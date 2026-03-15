import google.generativeai as genai

#GEMINI_API_KEY = "AIzaSyDwaF4JhBzrVg21vwzTrV-QKIRRD4-YQAA"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-flash-lite-latest")
