


# Productivity AI — Personal AI Assistant

<div align="center">

![Productivity AI](https://img.shields.io/badge/Productivity_AI-v2.0.0-8b5cf6?style=for-the-badge&logo=openai&logoColor=white)
![Google ADK](https://img.shields.io/badge/Google_ADK-Multi--Agent-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_2.0_Flash-LLM-34A853?style=for-the-badge&logo=google&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Deployed](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

**A multi-agent AI productivity system that manages your tasks, notes, research, and daily briefings through a beautiful conversational interface.**

🔗 **[Live Demo → productivity-ai.onrender.com](https://productivity-ai.onrender.com)**

</div>

---

## 📸 UI Preview

> Dark-themed chat interface inspired by modern AI assistants

```
┌─────────────────────────────────────────────────────────────────┐
│  Productivity AI     Personal Assistant   Gemini 2.0 Flash      │
│  ─────────────       ─────────────────────────────────────────  │
│  💬 Chat                                                         │
│  ☑️  Tasks          ┌─────────────────────────────────────────┐ │
│  ✨ Notes           │ ✓ Note saved                            │ │
│  🔍 Research        │ Title: Meeting                          │ │
│  ☀️  Daily Briefing │ Preview: We discussed AI features...    │ │
│                     │ ✦ Would you like me to summarize this?  │ │
│  RECENT             └─────────────────────────────────────────┘ │
│  · Meeting notes                                                 │
│  · Q4 project ideas  ┌─────────────────────────────────────┐    │
│  · ML findings       │ 🧠 AI Summary:                      │    │
│                      │ • Discussed AI-powered features      │    │
│  Vaishnavi K.        │ • Reviewed project deadlines         │    │
│  Pro Plan            │ • Identified UI improvements         │    │
│                      └─────────────────────────────────────┘    │
│  [ Ask me anything — tasks, notes, research, briefings... ] →   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture
```

```
<img width="1440" height="1102" alt="image" src="https://github.com/user-attachments/assets/08691071-21b8-410c-b246-145fb055fc32" />
 <img width="1440" height="762" alt="image" src="https://github.com/user-attachments/assets/380c247d-f081-4600-90cb-00816a1db690" />  
 
---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔴🟡🟢 **Priority tasks** | Create tasks with High/Medium/Low priority and due dates |
| 📌 **Smart notes** | Save notes with tags, retrieve, summarize into bullet points |
| 🔍 **Wikipedia research** | Search any topic, get cited summaries instantly |
| ☀️ **Daily briefing** | One prompt gives you all tasks + notes for the day |
| 🧠 **Session memory** | Remembers full conversation per user session |
| 💬 **Natural language** | No commands needed — just chat naturally |
| 🌙 **Dark UI** | Beautiful dark-themed interface, works on all devices |
| ⚡ **REST API** | Clean JSON API for all operations |

---

## 🤖 Agent Routing

```
"Add a high priority task..."      → task_agent  → create_task()
"Save a note titled Meeting..."    → notes_agent → save_note()
"Summarize note Meeting"           → notes_agent → summarize_note()
"What is machine learning?"        → search_agent → search_wikipedia()
"What's my day look like?"         → search_agent → get_daily_briefing()
"Search AI and save a note"        → search_agent + notes_agent (chained)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **AI Framework** | Google Agent Development Kit (ADK) |
| **LLM** | Gemini 2.0 Flash |
| **Backend** | FastAPI + Uvicorn |
| **Frontend** | Vanilla HTML/CSS/JS (dark theme) |
| **External Data** | Wikipedia REST API |
| **Deployment** | Render (Cloud) |
| **Language** | Python 3.11+ |

---

## 📁 Project Structure

```
PRODUCTIVITY-AI/
├── index.html              # Dark chat UI (auto-served at /)
├── main.py                 # FastAPI server + /chat endpoint
├── agent.py                # Root coordinator agent
├── agents/
│   ├── __init__.py
│   ├── task_agent.py       # Task management (create/list/complete/delete)
│   ├── notes_agent.py      # Notes (save/retrieve/summarize/search)
│   └── search_agent.py     # Research + daily briefing
├── requirements.txt
├── Dockerfile
├── render.yaml             # Render deployment config
└── .env.example
```

---

## 🚀 Quick Start

**1. Clone & install:**
```bash
git clone https://github.com/vaishnavi-ctrl-jpg/PRODUCTIVITY-AI
cd PRODUCTIVITY-AI
pip install -r requirements.txt
```

**2. Set up environment:**
```bash
cp .env.example .env
# Edit .env and add your Google AI Studio API key
# Get free key at: https://aistudio.google.com/apikey
```

**3. Run:**
```bash
python main.py
```

Open `http://localhost:8080` — UI loads automatically! ✨

---

## 🌐 API Reference

### `POST /chat`
```json
{
  "message": "Add a high priority task to submit the project by tomorrow",
  "session_id": "user123"
}
```

**Response:**
```json
{
  "reply": "✅ Task created\nTitle: Submit the project\nPriority: High\nDue: tomorrow",
  "session_id": "user123",
  "status": "success"
}
```

### `GET /health`
```json
{ "status": "healthy", "agent": "productivity_assistant", "version": "2.0.0" }
```

### `GET /sessions`
```json
{ "active_sessions": ["user123"], "count": 1 }
```

---

## ☁️ Deploy to Cloud Run

```bash
gcloud run deploy productivity-ai \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your-key,MODEL=gemini-2.0-flash
```

---

## 🏆 Built for APAC GenAI Academy — Cohort 1 Hackathon

**Participant:** Vaishnavi Kamthe
**Track:** Hackathon — Multi-Agent Productivity Assistant
**Problem Statement:** Build a multi-agent AI system that helps users manage tasks, schedules, and information by interacting with multiple tools and data sources.

**How it meets the criteria:**
- ✅ Primary agent coordinating sub-agents (root_agent → task/notes/search agents)
- ✅ Multiple tools via natural language (create_task, save_note, search_wikipedia, get_daily_briefing)
- ✅ Multi-step workflows (search + save, task + briefing)
- ✅ Session memory across conversation turns
- ✅ Deployed as API-based system on Render

---

<div align="center">

Made with 💜 by Vaishnavi Kamthe

![GitHub](https://img.shields.io/badge/GitHub-vaishnavi--ctrl--jpg-181717?style=flat&logo=github)

</div>
