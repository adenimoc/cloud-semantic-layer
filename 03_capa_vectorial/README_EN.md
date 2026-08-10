# 🔍 Vector Layer (Unstructured Semantic Context)

> **Design Signature:** Embeddings and unstructured context (`SQL` / Vector Store / `pgvector`).

---

## 🎯 Purpose of the Vector Layer
Retrieve information based on **semantic similarity** rather than exact keywords or rigid relational structures.

This is the cornerstone of **RAG (Retrieval-Augmented Generation)** systems for querying unstructured documentation: user manuals, refund policies, contracts, or FAQs.

---

## 🛠️ Typical Stack
* PostgreSQL + `pgvector` (Supabase / AWS Aurora)
* Dedicated Vector Stores: Qdrant, Pinecone, Milvus, Chroma
* Embeddings: OpenAI (`text-embedding-3-small`), Cohere Embed, HuggingFace BGE

---

## 💡 Golden Rules
1. **Do not use for accounting or relational queries:** Never ask the Vector Layer to calculate total monthly sales or guess corporate parent relationships.
2. **Smart chunking & metadata:** Pair every vector with structured metadata (`JSONB`) to enable hybrid filtering (`vector_search + metadata_filter`).
3. **Clear signatures:** Tables with data type `VECTOR(...)`, `HNSW` indexes, or cosine distance operators (`<=>`) = **Vector Layer**.

---

## 📂 Files in this section
* [`vector_store_setup.sql`](vector_store_setup.sql): DDL setup for `pgvector`, knowledge base table, and HNSW index.
