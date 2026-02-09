from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from datetime import timedelta
from dashboard.models import UserActivity
import json


@login_required
def whisper_home(request):
    return render(request, 'whisper/whisper.html')


@csrf_exempt
@login_required
def log_whisper_activity(request):
    if request.method == "POST":
        data = json.loads(request.body)
        word_count = data.get("word_count", 0)

        if word_count >= 100:

            # Prevent farming (once per day)
            today = now() - timedelta(days=1)

            already_logged = UserActivity.objects.filter(
                user=request.user,
                feature="Whisper",
                created_at__gte=today
            ).exists()

            if not already_logged:
                UserActivity.objects.create(
                    user=request.user,
                    feature="Whisper",
                    points=5
                )

        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "Invalid request"}, status=400)
