from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

print("=====TRANSLATION APP=====")


def main():
    while True:
        # For source language
        source = input("Enter source language (English/Hindi): ")
        source_lng_code = ""

        if source.lower() == "english":
            source_lng_code = "en-IN"
        elif source.lower() == "hindi":
            source_lng_code = "hi-IN"
        else:
            print("Invalid source language. Please enter either 'English' or 'Hindi'.")
            continue

        # For target language
        target = input("Enter target language (Tamil/Odia): ")
        target_lng_code = ""

        if target.lower() == "tamil":
            target_lng_code = "ta-IN"
        elif target.lower() == "odia":
            target_lng_code = "or-IN"
        else:
            print("Invalid target language. Please enter either 'Tamil' or 'Odia'.")
            continue

        user_input = input("\nEnter text to translate: ")
        print("Translating text...")

        response = client.text.translate(
            source_language_code=source_lng_code,
            target_language_code=target_lng_code,
            input=user_input,
            speaker_gender="Female"  # F should be capital
        )

        print(response.translated_text)

        user_interest = input("Do you want to translate more text? (yes/no): ")
        if user_interest.lower() != "yes":
            print("Exiting the translation app.")
            break


main()