from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import timedelta
from dashboard.models import UserActivity


@login_required
def mind_home(request):
    flashcards = []

    if request.method == "POST":
        text = request.POST.get("topic_text", "").strip()

        if text:
            sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
            points = []

            for s in sentences:
                parts = s.replace(":", "-").split("-")
                if len(parts) >= 2:
                    q = parts[0].strip()
                    a = "-".join(parts[1:]).strip()
                    points.append((q, a))
                else:
                    if len(s.split()) > 4:
                        q = s[:40].strip() + "…?"
                        a = s
                        points.append((q, a))

            for q, a in points:
                flashcards.append({"question": q, "answer": a})

            # 🔥 Activity-Based Scoring
            word_count = len(text.split())

            if word_count >= 50:

                today = now() - timedelta(days=1)

                already_logged = UserActivity.objects.filter(
                    user=request.user,
                    feature="Mind Garden",
                    created_at__gte=today
                ).exists()

                if not already_logged:
                    UserActivity.objects.create(
                        user=request.user,
                        feature="Mind Garden",
                        points=10
                    )

    return render(request, "mindgarden/mindgarden.html", {"flashcards": flashcards})
