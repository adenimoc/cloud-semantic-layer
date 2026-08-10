# 🤖 Agentic Layer (Real-Time Intent Routing)

> **Design Signature:** Traffic management and routing logic (`Python` / Intent Routers / `FastAPI`).

---

## 🎯 Purpose of the Agentic Layer
Serve as the **brain and front-desk receptionist** of the architecture.

When a user request arrives, the Agentic Layer **DOES NOT** try to answer directly by improvising code or hallucinating text. Its primary responsibility is to **catch the intent**, classify it with ultra-low latency (<20ms), and delegate the query to the appropriate specialized layer:
* If it asks for metrics -> Dispatch to **Metric Layer** (`Cube.dev`).
* If it asks for hierarchies/relationships -> Dispatch to **Ontological Layer** (`SQL / Graphs`).
* If it asks for manuals/guides -> Dispatch to **Vector Layer** (`pgvector / RAG`).

---

## 🛠️ Typical Stack
* `semantic-router` (Aurelio AI)
* `LangGraph` / `FastAPI` / `Pydantic AI`
* Lightweight embedding routers or high-precision regex matchers

---

## 💡 Golden Rules
1. **Surgical Boundaries:** The agentic layer never calculates math or guesses entity structures on its own.
2. **Ultra-Low Latency:** It must decide routing in milliseconds without calling heavy LLMs just for classification.
3. **Clear Signatures:** Python classification scripts (`agent_router.py`), intent routers, and orchestrators = **Agentic Layer**.

---

## 📂 Files in this section
* [`agent_router.py`](agent_router.py): Python intent router implementation (supports `semantic-router` and local fallback).
* [`requirements.txt`](requirements.txt): Required Python dependencies.
