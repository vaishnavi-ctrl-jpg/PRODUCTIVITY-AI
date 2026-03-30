import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from agents import task_agent, notes_agent, search_agent

load_dotenv()

root_agent = Agent(
    name="productivity_assistant",
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    description="Personal AI productivity assistant for tasks, notes, research, and daily briefings.",
    instruction="""
        You are a smart personal productivity assistant.

        Route requests to the correct sub-agent:
        - Tasks (create/list/complete/delete) → task_agent
        - Notes (save/get/list/summarize/search) → notes_agent
        - Research, Wikipedia, web pages → search_agent
        - "daily briefing", "what's my day", "morning update" → search_agent (get_daily_briefing)
        - Multi-step requests → use multiple agents in sequence

        Always confirm every action. Be direct, brief, and helpful.
        Remember full conversation context within the session.
    """,
    sub_agents=[task_agent, notes_agent, search_agent],
)
