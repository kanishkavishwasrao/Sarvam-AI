from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
)
from livekit.plugins import sarvam

load_dotenv()


class VoiceAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="""
            You are a helpful voice agent.
            Be helpful, concise, and provide accurate information.
            Speak naturally as if you are having a conversation with a human.
            """,
            stt=sarvam.STT(
                model="saaras:v3",
                mode="transcribe",
            ),
            llm=sarvam.LLM(
                model="sarvam-105b",
            ),
            tts=sarvam.TTS(
                model="bulbul:v3",
                target_language_code="en-IN",
            ),
        )

    async def on_enter(self):
        """Called when the agent enters the conversation."""
        self.session.generate_reply(instructions="Greet the user briefly.")


async def entrypoint(ctx: JobContext):
    session = AgentSession()

    await session.start(
        agent=VoiceAgent(),
        room=ctx.room,
    )
    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))