from sarvamai import SarvamAI
from sarvamai.play import play, save
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

def main():
    user_input = input("Enter text to convert to speech: ")
    print("Converting text to speech...")
    audio=client.text_to_speech.convert(
        model="bulbul:v3",
        language_code="en-IN",
        speaker="aayan",
        text=user_input,
        output_audio_codec="mp3"
    )

    #Save your audio
    #save(audio,"tts_audio.mp3")

    play(audio)
    
main()