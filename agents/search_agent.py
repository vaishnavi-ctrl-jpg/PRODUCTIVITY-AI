import os
import urllib.request
import urllib.parse
import json
from google.adk.agents import Agent


def search_wikipedia(query: str) -> dict:
    """Searches Wikipedia. Args: query (topic to search)."""
    encoded = urllib.parse.quote(query.replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ProductivityAI/2.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return {
                "status": "success",
                "topic": data.get("title", query),
                "summary": data.get("extract", "No results found."),
                "source": data.get("content_urls", {}).get("desktop", {}).get("page", "")
            }
    except Exception as e:
        return {"status": "error", "summary": f"Could not find results for '{query}'."}


def fetch_page(url: str) -> dict:
    """Fetches content from a URL. Args: url."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ProductivityAI/2.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            return {"status": "success", "url": url, "content": content[:2500]}
    except Exception as e:
        return {"status": "error", "content": f"Could not load: {str(e)}"}


def get_daily_briefing() -> dict:
    """Generates a daily briefing of all tasks and notes."""
    return {
        "status": "ok",
        "instruction": "Generate a daily briefing. Format EXACTLY as:\n☀️ Daily Briefing\n\n🔴 High Priority Tasks:\n- [tasks]\n\n🟡 Medium Priority Tasks:\n- [tasks]\n\n🟢 Low Priority Tasks:\n- [tasks]\n\n📌 Your Notes:\n- [note titles]\n\n💪 [one encouraging closing line]"
    }


search_agent = Agent(
    name="search_agent",
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    description="Searches Wikipedia, fetches web pages, generates daily briefings.",
    instruction="""
        You are a research and briefing assistant.

        For research results, format as:
        🔍 [Topic]
        [2-3 paragraph summary]
        Source: [URL]

        For daily briefings use EXACTLY:
        ☀️ Daily Briefing
        🔴 High Priority Tasks: [list]
        🟡 Medium Priority Tasks: [list]
        🟢 Low Priority Tasks: [list]
        📌 Your Notes: [list]
        💪 [encouraging line]

        Be factual, concise, always cite sources.
    """,
    tools=[search_wikipedia, fetch_page, get_daily_briefing],
)
