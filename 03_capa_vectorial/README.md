# 🔍 Capa Vectorial (Contexto Semántico Unstructured)

> **Firma de diseño:** Embeddings y contexto no estructurado (`SQL` / Vector Store / `pgvector`).

---

## 🎯 Objetivo de la Capa Vectorial
Recuperar información basada en **similitud de significado** en lugar de coincidencias exactas o relaciones rígidas.

Es la piedra angular de los sistemas **RAG (Retrieval-Augmented Generation)** para consultar documentación no estructurada: manuales de usuario, políticas de reembolso, contratos o preguntas frecuentes.

---

## 🛠️ Herramientas Típicas
* PostgreSQL + `pgvector` (Supabase / AWS Aurora)
* Base de datos vectoriales dedicadas: Qdrant, Pinecone, Milvus, Chroma
* Embeddings: OpenAI (`text-embedding-3-small`), Cohere Embed, HuggingFace BGE

---

## 💡 Reglas de Oro
1. **No usar para respuestas contables ni relacionales:** No le pidas a la Capa Vectorial calcular la suma de las ventas del mes ni adivinar de qué empresa es filial un cliente.
2. **Chunking inteligente y metadatos:** Acompaña cada vector con metadatos estructurados (`JSONB`) para poder hacer filtrado híbrido (`vector_search + metadata_filter`).
3. **Firmas claras:** Tablas con tipo de datos `VECTOR(...)`, índices `HNSW` o llamadas a funciones de distancia de coseno (`<=>`) = **Capa Vectorial**.

---

## 📂 Archivos en esta sección
* [`vector_store_setup.sql`](vector_store_setup.sql): Setup DDL de `pgvector`, tabla de base de conocimientos e índice HNSW.
