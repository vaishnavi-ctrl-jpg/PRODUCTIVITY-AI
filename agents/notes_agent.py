import os
from google.adk.agents import Agent


def save_note(title: str, content: str, tags: str = "") -> dict:
    """Saves a note. Args: title, content, tags (comma-separated, optional)."""
    return {
        "status": "note_saved",
        "title": title,
        "content": content,
        "tags": tags if tags else "none",
        "preview": content[:120] + "..." if len(content) > 120 else content
    }


def get_note(title: str) -> dict:
    """Gets a note by title. Args: title."""
    return {"status": "ok", "instruction": f"Find and display the full note titled '{title}' from conversation history."}


def list_notes() -> dict:
    """Lists all saved notes."""
    return {"status": "ok", "instruction": "List all notes saved in this session with titles and tags."}


def summarize_note(title: str) -> dict:
    """Summarizes a note into bullet points. Args: title."""
    return {"status": "ok", "instruction": f"Find the note '{title}' and summarize it in exactly 3 bullet points. Format as: 🧠 AI Summary: followed by bullet points."}


def search_notes(keyword: str) -> dict:
    """Searches notes by keyword. Args: keyword."""
    return {"status": "ok", "keyword": keyword, "instruction": f"Find all notes containing '{keyword}' from session history."}


notes_agent = Agent(
    name="notes_agent",
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    description="Saves, retrieves, lists, summarizes, and searches notes.",
    instruction="""
        You are a notes assistant.

        When a note is saved, respond EXACTLY in this format:
        📌 Note saved
        Title: [title]
        Tags: [tags or none]
        Preview: [first 100 chars of content]

        When summarizing, respond EXACTLY in this format:
        🧠 AI Summary:
        • [point 1]
        • [point 2]
        • [point 3]

        Always confirm saves. Be organized and brief.
    """,
    tools=[save_note, get_note, list_notes, summarize_note, search_notes],
)
