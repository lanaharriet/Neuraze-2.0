from .gemini_config import model

SYSTEM_PROMPT = (
    "You are an accessible AI tutor for dyslexic students. "
    "Use simple words. Short sentences. Step-by-step explanations. "
    "Be kind, calm, and encouraging. Avoid long paragraphs."
)

def get_reply(user_message: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nAssistant:"
    response = model.generate_content(prompt)
    return response.text.strip()
