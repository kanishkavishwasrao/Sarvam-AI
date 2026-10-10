from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

def main():
    print("Converting text to speech...")
    chunks = []
    for chunk in client.text_to_speech.convert_stream(
        model="bulbul:v3",
        language_code="en-IN",
        speaker="ritu",
        text="Hello I am Ritu. I stay in Pune.",
        output_audio_codec="mp3"
    ):
        chunks.append(chunk)

    audio = b"".join(chunks)

    filename = "stream_audio.mp3"
    with open(filename, "wb") as f:
        f.write(audio)

    print(f"Saved {filename} ({len(audio)} bytes)")
    print("Playing audio...")
    os.startfile(filename)

main()