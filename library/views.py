from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.timezone import now
from datetime import timedelta
from xhtml2pdf import pisa

from dashboard.models import UserActivity


@login_required
def library_home(request):
    reading_text = ""

    if request.method == "POST":
        reading_text = request.POST.get("reading_text", "").strip()

        word_count = len(reading_text.split())

        # 🔥 Activity-Based Scoring
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

        # 📄 Download PDF logic
        if "download_pdf" in request.POST:
            template = get_template("library/library_pdf.html")
            html = template.render({"reading_text": reading_text})
            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="LibraryGate.pdf"'

            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse("Error generating PDF")
            return response

    return render(request, "library/library.html", {"reading_text": reading_text})
