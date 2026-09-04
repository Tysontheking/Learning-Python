import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print(api_key is not None)

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in .env")


client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.6-flash"
)

while True:
    user_question = input("Question : ")

    if user_question.lower() == "exit":
        print("Bot: Goodbye!")
        break
    else:
        response = chat.send_message(
            message=user_question
        )
        
        print("Bot : ",response.text)



