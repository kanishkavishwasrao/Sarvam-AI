from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

def main():
    print("====Kanishka's Chatbot====")

    messages = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions(
            model="sarvam-105b",
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print("Jarvis:", reply + "\n")

main()