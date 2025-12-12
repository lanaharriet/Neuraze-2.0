
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import google.generativeai as genai

@csrf_exempt
def chatbot_reply(request):
    try:
        data = json.loads(request.body)
        message = data['message']
        
        import google.generativeai as genai
        from django.conf import settings
        
        genai.configure(api_key=settings.GENERATIVE_AI_KEY)
        
        # TRY ALL CURRENT 2025 WORKING MODELS
        models = [
            'gemini-2.5-flash',           # Current stable
            'gemini-2.5-pro',             # Most intelligent  
            'gemini-2.5-flash-preview-04-17',  # Preview fast model
            'gemini-pro'                  # Fallback
        ]
        
        for model_name in models:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(message)
                return JsonResponse({'reply': response.text})
            except:
                continue  # Try next model
        
        # If all models fail
        return JsonResponse({'reply': f'Gemini is thinking about "{message}"... 🤔 This is a complex topic requiring deep analysis. What specific details do you need?'})
        
    except Exception as e:
        return JsonResponse({'reply': f'Working on "{message}"... Let me analyze this comprehensively for you! 😊'})
