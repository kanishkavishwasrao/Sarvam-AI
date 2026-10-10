from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = client.chat.completions(
            model="sarvam-105b",
            messages=[{"role": "user", "content": user_input}]
        )

        print("Jarvis:", response.choices[0].message.content)

main()