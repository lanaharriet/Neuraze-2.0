import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyBBp-e1A0z3qPadiyl4cbynvF1o31y-lDs"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-flash-lite-latest")
