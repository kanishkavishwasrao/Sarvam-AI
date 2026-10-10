from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

def main():
    response=client.text.translate(
        source_language_code="en-IN",
        target_language_code="hi-IN",
        input="Hello I am Ritu. I stay in Pune.",
        speaker_gender="Female" #F should be capital. I wrote female it threw an error.
    )

    print(response.translated_text)

main()