from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.timezone import now
from datetime import timedelta

import pdfplumber
from docx import Document
from xhtml2pdf import pisa

from dashboard.models import UserActivity



def extract_text_from_file(uploaded_file):
    filename = uploaded_file.name.lower()
    text_chunks = []

    
    uploaded_file.seek(0)

  
    if filename.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text(
                    layout=True,
                    x_tolerance=1,
                    y_tolerance=1
                )
                if page_text:
                    text_chunks.append(page_text)

    elif filename.endswith(".docx"):
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            if para.text.strip():
                text_chunks.append(para.text)

    return "\n\n".join(text_chunks).strip()



@login_required
def library_home(request):
    reading_text = ""

    if request.method == "POST":
        uploaded_file = request.FILES.get("upload_file")

        # 📂 File upload takes priority
        if uploaded_file:
            reading_text = extract_text_from_file(uploaded_file)
        else:
            reading_text = request.POST.get("reading_text", "").strip()

        # 🧠 SAFETY: prevent None or partial results
        if not reading_text:
            reading_text = ""

        # 🔥 Activity-based scoring
        word_count = len(reading_text.split())

        if word_count >= 50:
            today = now() - timedelta(days=1)
            already_logged = UserActivity.objects.filter(
                user=request.user,
                feature="Library",
                created_at__gte=today
            ).exists()

            if not already_logged:
                UserActivity.objects.create(
                    user=request.user,
                    feature="Library",
                    points=5
                )

        
        if "download_pdf" in request.POST:
            template = get_template("library/library_pdf.html")
            html = template.render({"reading_text": reading_text})

            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = (
                'attachment; filename="LibraryGate.pdf"'
            )

            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse("Error generating PDF")

            return response

    return render(request, "library/library.html", {
        "reading_text": reading_text
    })
