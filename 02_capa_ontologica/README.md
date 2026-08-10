# 🌐 Capa Ontológica (Entidades y Jerarquías)

> **Firma de diseño:** Esquemas de relaciones y quién es quién (`JSON` / `SQL` / Grafos).

---

## 🎯 Objetivo de la Capa Ontológica
Enseñar al agente la **estructura del mundo real** y el mapa de entidades del dominio:
* ¿Quién es quién?
* ¿De quién depende esta entidad?
* ¿Cuáles son las jerarquías y restricciones semánticas?

A diferencia de la búsqueda semántica no estructurada, las relaciones ontológicas son **deterministas y basadas en grafos/Foreign Keys**. 

---

## 🛠️ Herramientas Típicas
* PostgreSQL / Supabase (Tablas relacionales con comentarios semánticos `COMMENT ON`)
* Neo4j / Memgraph (Bases de datos de Grafos con Cypher)
* JSON-LD / OWL (Web Semántica)

---

## 💡 Reglas de Oro
1. **Evitar adivinanzas semánticas:** Si la pregunta del usuario es *"¿Qué clientes pertenecen a la Organización X?"*, la respuesta sale de un `JOIN` determinista o una travesía en grafo, NUNCA de un RAG/Embedding.
2. **Enriquecer con `COMMENT ON`:** En Postgres, los comentarios DDL sirven como metadatos explícitos para que el agente entienda el propósito de cada tabla y columna.
3. **Jerarquías estrictas:** Utiliza claves foráneas (`FOREIGN KEY`) e índices explícitos.

---

## 📂 Archivos en esta sección
* [`schema_ontologia.sql`](schema_ontologia.sql): DDL completo en Postgres con relaciones entre Organizaciones, Clientes y Ventas.
