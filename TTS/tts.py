from sarvamai import SarvamAI
from sarvamai.play import save
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

def main():
    audio=client.text_to_speech.convert(
        model="bulbul:v3",
        language_code="en-IN",
        speaker="aayan",
        text="Hello My name is Aayan.",
        output_audio_codec="mp3"
    )

    save(audio,"tts_audio.mp3")

main()