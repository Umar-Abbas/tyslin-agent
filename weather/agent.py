from google.adk.agents import Agent
from .tools import get_weather

root_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash",
    description="A bot that can get the weather.",
    tools=[get_weather],
)
