from ai_chatbot.gemini_config import model

response = model.generate_content("Say hello in one short sentence")
print(response.text)
