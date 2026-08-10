# 🧭 The Architect's Compass: 4-Layer Architecture for AI Agents

[Español](README.md) | **English**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-4--Layer%20Agentic-emerald.svg)](#-engineering-setting-the-boundaries)
[![GitHub Repository](https://img.shields.io/badge/GitHub-cloud--semantic--layer-181717.svg?logo=github)](https://github.com/adenimoc/cloud-semantic-layer)

> **Educational & hands-on practice repository for the 4-layer AI Agent architecture: Metric, Ontological, Vector, and Agentic.**

To keep from getting lost (and to prevent the LLM from hallucinating), the entire team —from junior engineers to stakeholders— must understand which layer we are standing on. The golden rule is simple: **every technical process is assigned a specific "design signature"**:

* 📊 **Metric Layer:** Pure math and business rules files (`YAML` / `Cube`).
* 🌐 **Ontological Layer:** Relationship schemas and entity definitions (`JSON` / `SQL` / Graphs).
* 🔍 **Vector Layer:** Embeddings and unstructured semantic context (`SQL` / Vector Store).
* 🤖 **Agentic Layer:** Traffic routing and intent dispatching (`Python` / Routers).

---

## 📌 Table of Contents
1. [🏛️ Real-World Analogy: The Smart Building](#️-real-world-analogy-the-smart-building)
2. [⚙️ Engineering: Setting the Boundaries](#️-engineering-setting-the-boundaries)
3. [📁 Repository Structure](#-repository-structure)
4. [🧩 The 4 Layers Explained](#-the-4-layers-explained)
   * [1. Metric Layer](#-1-metric-layer-deterministic-numerical-rules)
   * [2. Ontological Layer](#-2-ontological-layer-entities--hierarchies)
   * [3. Vector Layer](#-3-vector-layer-unstructured-semantic-context)
   * [4. Agentic Layer](#-4-agentic-layer-real-time-routing)
5. [🚨 The Deadly Trap: Layer Bleeding](#-the-deadly-trap-layer-bleeding)
6. [🚀 Quickstart (Hands-on)](#-quickstart-hands-on)
7. [📜 License](#-license)

---

## 🏛️ Real-World Analogy: The Smart Building

Imagine you are constructing a smart building from scratch:

* 📊 **Metric Layer (Structural Blueprints):** Here you define raw numbers. Column measurements, load-bearing capacities. Zero room for interpretation.
* 🌐 **Ontological Layer (Pipes & Wiring):** You map how kitchen water connects to the main bathroom. These are fixed dependencies and hierarchies (who connects to whom).
* 🔍 **Vector Layer (Historical Blueprint Library):** Imagine a huge stack of scanned blueprints. You organize them by "visual similarity" to quickly retrieve matching documents.
* 🤖 **Agentic Layer (Front Desk Receptionist):** The person standing in the lobby. A visitor arrives and says *"I'm here to fix the lights"*. The receptionist (without attempting to fix the lights themselves) parses the intent and routes the visitor directly to the electrician using blueprints from the previous phases.

---

## ⚙️ Engineering: Setting the Boundaries

This is how the flow looks in code. When you open any file in the repository, you should immediately know which layer it belongs to.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                    ROUTING AND DISPATCHING PHASE                       │
│ 🤖 1. AGENTIC LAYER (Semantic Router in Python)                        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
┌─────────────────┐        ┌──────────────────┐       ┌──────────────────┐
│DETERMINISTIC    │        │ CONTEXTUAL PHASE │        │ RELATIONAL PHASE │
│   PHASE         │        │ 🔍 3. VECTOR     │        │ 🌐 4. ONTOLOGICAL│
│ 📊 2. METRIC    │        │    LAYER         │        │    LAYER         │
│    LAYER        │        │ (Supabase Vector)│        │ (JSON-LD/Graph)  │
│ (YAML / Cube)   │        └──────────────────┘        └──────────────────┘
└─────────────────┘
```

---

## 📁 Repository Structure

```text
.
├── README.md                      # Spanish Documentation & Main Architecture Guide
├── README_EN.md                   # English Documentation & Main Architecture Guide
├── LICENSE                        # Project License (MIT)
├── .gitignore                     # Git exclusion rules
├── 01_capa_metrica/               # 📊 Metric Layer: Immutable business rules and formulas
│   ├── README.md                  # Metric layer guide (Spanish)
│   ├── README_EN.md               # Metric layer guide (English)
│   └── model/cubes/Ventas.yml     # Semantic metric definition in Cube.dev
├── 02_capa_ontologica/            # 🌐 Ontological Layer: Entity relationships & taxonomies
│   ├── README.md                  # Ontology guide (Spanish)
│   ├── README_EN.md               # Ontology guide (English)
│   └── schema_ontologia.sql       # Postgres DDL with semantic comments
├── 03_capa_vectorial/             # 🔍 Vector Layer: Embeddings and unstructured context
│   ├── README.md                  # Vector & RAG guide (Spanish)
│   ├── README_EN.md               # Vector & RAG guide (English)
│   └── vector_store_setup.sql     # pgvector setup DDL and knowledge base table
├── 04_capa_agentica/              # 🤖 Agentic Layer: Intent routing and orchestration
│   ├── README.md                  # Agentic layer guide (Spanish)
│   ├── README_EN.md               # Agentic layer guide (English)
│   ├── agent_router.py            # Python router with Semantic Router & local fallback
│   └── requirements.txt           # Python dependencies
└── scripts/
    └── demo_orquestador.py        # Interactive CLI demo to test real-time intent routing
```

---

## 🧩 The 4 Layers Explained

### 📌 1. METRIC LAYER (Deterministic Numerical Rules)

* **Where does it live?:** Cube.dev, dbt, or Semantic Layer.
* **Which file is it?:** `01_capa_metrica/model/cubes/Ventas.yml`
* **What is it for?:** Ensuring the LLM **never** guesses math or improvises a `GROUP BY` in SQL.

```yaml
# ==========================================
# 📊 METRIC LAYER: IMMUTABLE RULES
# ==========================================
cubes:
  - name: Ventas
    sql_table: public.ventas

    measures:
      # We declare absolute business truth here
      - name: ventas_netas
        title: "Net Sales"
        type: sum
        sql: "monto - descuento"
        filters:
          - sql: "{CUBE}.estado = 'completada'"

    dimensions:
      - name: estado
        type: string
        sql: estado
```

💡 **Pro tip:** If you are writing `sum`, `count`, or formulas in a YAML file, you are building the **Metric Layer**.

---

### 📌 2. ONTOLOGICAL LAYER (Entities & Hierarchies)

* **Where does it live?:** Postgres (Supabase) or graph databases like Neo4j.
* **Which file is it?:** `02_capa_ontologica/schema_ontologia.sql`
* **What is it for?:** Teaching the agent world structure: who depends on whom and how entities relate.

```sql
-- =============================================
-- 🌐 ONTOLOGICAL LAYER: WHO IS WHO?
-- =============================================

CREATE TABLE public.organizaciones (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE public.clientes (
    id BIGSERIAL PRIMARY KEY,
    organizacion_id BIGINT REFERENCES public.organizaciones(id), -- Ownership relationship
    tipo_cliente TEXT NOT NULL CHECK (tipo_cliente IN ('enterprise', 'pyme', 'individual'))
);

-- Embed semantic metadata comments for LLM / Semantic Engines
COMMENT ON TABLE public.clientes IS 'Ontology: Consumer entity. Belongs to a parent Organization.';
```

💡 **Pro tip:** Foreign Keys, taxonomies, or maps like "X is a subsidiary of Y" = **Ontological Layer**.

---

### 📌 3. VECTOR LAYER (Unstructured Semantic Context)

* **Where does it live?:** Supabase (`pgvector`), Qdrant, Pinecone.
* **Which file is it?:** `03_capa_vectorial/vector_store_setup.sql` or RAG ingestion script.
* **What is it for?:** Searching by "meaning" or "similarity", not exact matches.

```sql
-- =============================================
-- 🔍 VECTOR LAYER: SIMILARITY SEARCH
-- =============================================

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE public.documentos_kb (
    id BIGSERIAL PRIMARY KEY,
    contenido TEXT NOT NULL,
    categoria_semantica TEXT, 
    pregunta_hipotetica TEXT,
    embedding VECTOR(1536) -- Dense vector search / embeddings
);
```

💡 **Pro tip:** Dimensions, `VECTOR(1536)`, PDF chunking, or RAG metadata = **Vector Layer**.

---

### 📌 4. AGENTIC LAYER (Real-Time Routing)

* **Where does it live?:** Your API (`FastAPI`, `LangGraph`, `Pydantic AI`).
* **Which file is it?:** `04_capa_agentica/agent_router.py`
* **What is it for?:** It is the brain. It catches user prompts and decides which of the other 3 layers to dispatch them to.

```python
# =============================================
# 🤖 AGENTIC LAYER: TRAFFIC & DECISION MAKING
# =============================================
from semantic_router import Route, RouteLayer
from semantic_router.encoders import OpenAIEncoder

# 1. Define intent boundaries
ruta_metrica = Route(
    name="CAPA_METRICA",
    utterances=["What are the total net sales?", "Show financial margin"]
)

ruta_vectorial = Route(
    name="CAPA_VECTORIAL",
    utterances=["How do I request a refund?", "Search service manuals"]
)

ruta_ontologica = Route(
    name="CAPA_ONTOLOGICA",
    utterances=["Which clients belong to Organization X?", "Show corporate structure"]
)

# 2. Initialize router (<20ms routing latency)
encoder = OpenAIEncoder()
router = RouteLayer(encoder=encoder, routes=[ruta_metrica, ruta_vectorial, ruta_ontologica])

# 3. Orchestration logic
def orquestar_consulta(prompt_usuario: str):
    intencion = router(prompt_usuario)
    print(f"\n[🤖 Agentic Layer] Intent: '{intencion.name}'")
    
    if intencion.name == "CAPA_METRICA":
        return "📊 Dispatching to Cube.dev (Metric Layer)..."
    elif intencion.name == "CAPA_VECTORIAL":
        return "🔍 Dispatching to Supabase pgvector (Vector Layer)..."
    elif intencion.name == "CAPA_ONTOLOGICA":
        return "🌐 Dispatching to Graph/Relational SQL (Ontological Layer)..."
    else:
        return "⚪ Standard LLM response..."
```

💡 **Pro tip:** Prompt classification, ultra-low latency routers, or state graphs = **Agentic Layer**.

---

## 🚨 The Deadly Trap: Layer Bleeding

The most common mistake when building agentic systems is blurring layer responsibilities. For instance:

1. Using the **Vector Layer** (RAG) to guess ontological questions (e.g., trying to "guess" via embeddings which subsidiary belongs to which company instead of performing a relational `JOIN`/Graph traversal).
2. Allowing the **Agentic Layer** to calculate sales metrics inside ad-hoc Python code.

**Keep each layer strictly in its boundary. Surgical boundaries = Robust systems.**

---

## 🚀 Quickstart (Hands-on)

### 1. Clone the repository
```bash
git clone https://github.com/adenimoc/cloud-semantic-layer.git
cd cloud-semantic-layer
```

### 2. Test the Agentic Layer (Interactive CLI Demo)
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r 04_capa_agentica/requirements.txt

# Run interactive orchestrator demo
python scripts/demo_orquestador.py
```

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
