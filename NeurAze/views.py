from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ai_chatbot.ai_speak import get_reply

@csrf_exempt
def chatbot_reply(request):
    if request.method != "POST":
        return JsonResponse({"reply": "Please send a message."})

    try:
        data = json.loads(request.body.decode("utf-8"))
        message = data.get("message", "").strip()

        if not message:
            return JsonResponse({"reply": "Please type a message."})

        reply = get_reply(message)
        return JsonResponse({"reply": reply})

    except Exception as e:
        return JsonResponse({
            "reply": "Sorry, I had trouble answering that. Please try again."
        })
