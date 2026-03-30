import os
from google.adk.agents import Agent


def create_task(title: str, priority: str = "medium", due_date: str = "") -> dict:
    """Creates a new task. Args: title, priority (low/medium/high), due_date (optional)."""
    return {
        "status": "task_created",
        "title": title,
        "priority": priority,
        "due_date": due_date if due_date else "no due date",
        "done": False
    }


def list_tasks() -> dict:
    """Lists all tasks from the session."""
    return {"status": "ok", "instruction": "List all tasks created in this session with their priority and due dates. Format with priority emojis: 🔴 High, 🟡 Medium, 🟢 Low."}


def complete_task(title: str) -> dict:
    """Marks a task as complete. Args: title of the task."""
    return {"status": "completed", "task_title": title}


def delete_task(title: str) -> dict:
    """Deletes a task. Args: title of the task."""
    return {"status": "deleted", "task_title": title}


def filter_tasks_by_priority(priority: str) -> dict:
    """Filters tasks by priority. Args: priority (low/medium/high)."""
    return {"status": "ok", "priority": priority, "instruction": f"List only {priority} priority tasks from session history."}


task_agent = Agent(
    name="task_agent",
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    description="Manages tasks — create, list, complete, delete, filter by priority.",
    instruction="""
        You are a task management assistant.

        When a task is created, respond EXACTLY in this format:
        📌 Note saved
        Title: [title]
        Priority: [priority]
        Due: [due date]

        When listing tasks use:
        🔴 High Priority:
        - [task] (due: [date])
        🟡 Medium Priority:
        - [task]
        🟢 Low Priority:
        - [task]

        Always confirm every action. Be brief and direct.
    """,
    tools=[create_task, list_tasks, complete_task, delete_task, filter_tasks_by_priority],
)
