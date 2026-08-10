# 🌐 Ontological Layer (Entities & Hierarchies)

> **Design Signature:** Relationship schemas and entity maps (`JSON` / `SQL` / Graphs).

---

## 🎯 Purpose of the Ontological Layer
Teach the agent **domain real-world structure** and entity relationships:
* Who is who?
* Which parent organization does this entity belong to?
* What are the strict taxonomies and relationships?

Unlike unstructured semantic vector searches, ontological relationships are **deterministic and graph/Foreign Key based**.

---

## 🛠️ Typical Stack
* PostgreSQL / Supabase (Relational tables with `COMMENT ON` semantic metadata)
* Neo4j / Memgraph (Graph Databases with Cypher)
* JSON-LD / OWL (Semantic Web)

---

## 💡 Golden Rules
1. **Avoid semantic guessing:** If the user asks *"Which clients belong to Organization X?"*, the answer comes from a deterministic `JOIN` or graph traversal, NEVER from RAG/Embeddings.
2. **Enrich with `COMMENT ON`:** In Postgres, DDL comments act as explicit metadata for the agent to understand table and column semantics.
3. **Strict hierarchies:** Use explicit foreign keys (`FOREIGN KEY`) and schema constraints.

---

## 📂 Files in this section
* [`schema_ontologia.sql`](schema_ontologia.sql): Complete Postgres DDL with relationships between Organizations, Clients, and Sales.
