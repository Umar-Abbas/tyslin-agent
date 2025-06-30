from google.adk.agents import Agent
from .tools import get_time

root_agent = Agent(
    name="time_agent",
    model="gemini-2.0-flash",
    description="A bot that can get the time.",
    tools=[get_time],
)
