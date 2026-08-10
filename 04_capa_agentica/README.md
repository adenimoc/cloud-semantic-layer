# 🤖 Capa Agéntica (Enrutamiento en Tiempo Real)

> **Firma de diseño:** El tráfico y las reglas de enrutamiento (`Python` / Routers de Intenciones / `FastAPI`).

---

## 🎯 Objetivo de la Capa Agéntica
Ser el **cerebro y recepcionista** de la arquitectura.

Cuando llega una solicitud del usuario, la Capa Agéntica **NO** intenta responderla directamente improvisando código ni haciendo alucinaciones. Su labor principal es **atrapar la intención**, clasificarla con latencia ultra-baja (<20ms) y delegar la consulta a la capa especializada correspondiente:
* Si pide métricas -> Despacha a **Capa Métrica** (`Cube.dev`).
* Si pide jerarquías/relaciones -> Despacha a **Capa Ontológica** (`SQL / Grafos`).
* Si pide manuales/guías -> Despacha a **Capa Vectorial** (`pgvector / RAG`).

---

## 🛠️ Herramientas Típicas
* `semantic-router` (Aurelio AI)
* `LangGraph` / `FastAPI` / `Pydantic AI`
* Routers por embeddings ligeros o regex de alta precisión

---

## 💡 Reglas de Oro
1. **Límites Quirúrgicos:** La capa agéntica jamás calcula sumas ni adivina jerarquías por su cuenta.
2. **Latencia Ultra-Baja:** Debe decidir el camino en milisegundos sin invocar un LLM pesado para clasificar.
3. **Firmas claras:** Scripts de clasificación de rutas en Python (`agent_router.py`), routers de intenciones y orquestadores = **Capa Agéntica**.

---

## 📂 Archivos en esta sección
* [`agent_router.py`](agent_router.py): Implementación del router de intenciones en Python (soporta `semantic-router` y fallback local).
* [`requirements.txt`](requirements.txt): Dependencias de Python necesarias.
