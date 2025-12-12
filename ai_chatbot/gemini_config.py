import google.generativeai as genai


GEMINI_API_KEY = "AIzaSyBwg1JynzfqKqz_JtlTseEL-3niZL8xsKY"

genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")
