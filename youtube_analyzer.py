from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

load_dotenv()

def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YouTubeTools()],
        instructions=dedent("""
            You are an expert YouTube content analyst.
            Create timestamps and summarize videos accurately.
        """),
        add_datetime_to_context=True,
        markdown=True,
    )

youtube_agent = build_youtube_agent()

youtube_agent.print_response(
    "Analyze this video: https://www.youtube.com/watch?v=OQCjakjCJu4&list=PLmXKhU9FNesSmu-_DKC7APRoFkaQvGurx",
    stream=True,
)