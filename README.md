# Arquitectura de 4 Capas para Agentes de IA

**Español** | [English](README_EN.md)

[![Purpose: Educational](https://img.shields.io/badge/Purpose-Educational%20%26%20Open-orange.svg)](#-comunidad-uso-educativo-y-recomendaciones)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-4--Layer%20Agentic-emerald.svg)](#-la-ingeniería-marcando-las-fronteras)
[![GitHub Repository](https://img.shields.io/badge/GitHub-cloud--semantic--layer-181717.svg?logo=github)](https://github.com/adenimoc/cloud-semantic-layer)

> **Repositorio de práctica y referencia educativa sobre la arquitectura de 4 capas para Agentes de IA: Métrica, Ontológica, Vectorial y Agéntica.**


Para no perdernos (ni hacer que el LLM delire), necesitamos que todo el equipo —desde el *junior* hasta el *stakeholder*— entienda en qué capa estamos parados. La regla de oro es simple: **a cada proceso técnico le asignamos una "firma de diseño"**:

* 📊 **Capa Métrica:** Archivos de reglas y matemática pura (`YAML` / `Cube`). Incluye el **Generador de Reportes Ejecutivos Automáticos**.
* 🌐 **Capa Ontológica:** Esquemas de relaciones y quién es quién (`JSON` / `SQL` / Grafos).
* 🔍 **Capa Vectorial:** Embeddings y contexto no estructurado (`SQL` / Vector Store).
* 🤖 **Capa Agéntica:** El tráfico, **Guardrails de Seguridad contra Prompt Injection** y reglas de enrutamiento (`Python` / Routers).


---

## 📌 Tabla de Contenidos
1. [🏛️ Bajándolo a la vida real: La analogía del Edificio Inteligente](#️-bajándolo-a-la-vida-real-la-analogía-del-edificio-inteligente)
2. [⚙️ La Ingeniería: Marcando las Fronteras](#️-la-ingeniería-marcando-las-fronteras)
3. [📁 Estructura del Repositorio](#-estructura-del-repositorio)
4. [🧩 Detalle de las 4 Capas](#-detalle-de-las-4-capas)
   * [1. Capa Métrica](#-1-capa-métrica-reglas-numéricas-deterministas)
   * [2. Capa Ontológica](#-2-capa-ontológica-entidades-y-jerarquías)
   * [3. Capa Vectorial](#-3-capa-vectorial-contexto-semántico-unstructured)
   * [4. Capa Agéntica](#-4-capa-agéntica-enrutamiento-en-tiempo-real)
5. [🚨 La Trampa Mortal: Layer Bleeding](#-la-trampa-mortal-layer-bleeding-solapamiento)
6. [🚀 Inicio Rápido (Hands-on)](#-inicio-rápido-hands-on)
7. [📜 Licencia](#-licencia)

---

## 🏛️ Bajándolo a la vida real: La analogía del Edificio Inteligente

Imagínate que estás construyendo un edificio inteligente desde cero:

* 📊 **Capa Métrica (Los Planos Estructurales):** Aquí defines los números fríos. Cuánto mide la columna, cuántos kilos de carga aguanta. Nada de interpretaciones.
* 🌐 **Capa Ontológica (Tuberías y Cableado):** Conectas cómo el agua de la cocina llega al baño principal. Son las dependencias y jerarquías (quién está conectado con quién).
* 🔍 **Capa Vectorial (La Biblioteca de Planos Históricos):** Imagina una pila gigantesca de planos escaneados. Los organizas por "parecido visual" para encontrar rápido cualquier documento parecido.
* 🤖 **Capa Agéntica (El Recepcionista de la Entrada):** El tipo parado en el lobby. Llega un visitante, dice *"vengo a reparar la luz"* y el recepcionista (sin intentar arreglar la luz él mismo) lee la intención y lo manda directo con el electricista usando los planos de las fases anteriores.

---

## ⚙️ La Ingeniería: Marcando las Fronteras

Así se ve el flujo en código. La idea es que cuando abras un archivo en el repo, sepas exactamente a qué capa pertenece.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   FASE DE ENRUTAMIENTO Y ASIGNACIÓN                    │
│ 🤖 1. CAPA AGÉNTICA (Semantic Router en Python)                        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
┌─────────────────┐        ┌──────────────────┐       ┌──────────────────┐
│ FASE DETERMINISTA│        │ FASE CONTEXTUAL  │       │ FASE RELACIONAL  │
│ 📊 2. CAPA      │        │ 🔍 3. CAPA       │       │ 🌐 4. CAPA       │
│    MÉTRICA      │        │    VECTORIAL     │       │    ONTOLÓGICA    │
│ (YAML / Cube)   │        │ (Supabase Vector)│       │ (JSON-LD/Graph)  │
└─────────────────┘        └──────────────────┘       └──────────────────┘
```

---

## 📁 Estructura del Repositorio

```text
.
├── README.md                      # La Brújula del Arquitecto (Documentación Principal)
├── LICENSE                        # Licencia del proyecto (MIT)
├── .gitignore                     # Configuración de exclusiones Git
├── 01_capa_metrica/               # 📊 Capa Métrica: Reglas y fórmulas numéricas inmutables
│   ├── README.md                  # Explicación y buenas prácticas de la Capa Métrica
│   └── model/cubes/Ventas.yml     # Definición semántica de métricas en Cube.dev
├── 02_capa_ontologica/            # 🌐 Capa Ontológica: Relaciones de entidades y taxonomías
│   ├── README.md                  # Guía de relaciones, Foreign Keys y grafos
│   └── schema_ontologia.sql       # DDL Postgres con metadatos semánticos
├── 03_capa_vectorial/             # 🔍 Capa Vectorial: Embeddings y contexto no estructurado
│   ├── README.md                  # Guía de RAG, pgvector y chunking
│   └── vector_store_setup.sql     # Setup de pgvector y tabla de conocimiento
├── 04_capa_agentica/              # 🤖 Capa Agéntica: Routers de intenciones y orquestación
│   ├── README.md                  # Guía de enrutamiento y orquestación
│   ├── agent_router.py            # Implementación en Python con Semantic Router
│   └── requirements.txt           # Dependencias necesarias
└── scripts/
    └── demo_orquestador.py        # Demo interactiva en CLI para probar el enrutamiento
```

---

## 🧩 Detalle de las 4 Capas

### 📌 1. CAPA MÉTRICA (Reglas Numéricas Deterministas)

* **¿Dónde vive?:** En Cube.dev, dbt o Semantic Layer.
* **¿Qué archivo es?:** `01_capa_metrica/model/cubes/Ventas.yml`
* **¿Para qué sirve?:** Para que el LLM **jamás** invente la matemática ni improvise un `GROUP BY` en SQL.

```yaml
# ==========================================
# 📊 CAPA MÉTRICA: REGLAS INMUTABLES
# ==========================================
cubes:
  - name: Ventas
    sql_table: public.ventas

    measures:
      # Aquí declaramos la verdad absoluta del negocio
      - name: ventas_netas
        title: "Ventas Netas"
        type: sum
        sql: "monto - descuento"
        filters:
          - sql: "{CUBE}.estado = 'completada'"

    dimensions:
      - name: estado
        type: string
        sql: estado
```

💡 **Tip rápido:** Si estás escribiendo `sum`, `count`, o fórmulas en un YAML, estás construyendo **Capa Métrica**.

---

### 📌 2. CAPA ONTOLÓGICA (Entidades y Jerarquías)

* **¿Dónde vive?:** En Postgres (Supabase) o motores de grafos tipo Neo4j.
* **¿Qué archivo es?:** `02_capa_ontologica/schema_ontologia.sql`
* **¿Para qué sirve?:** Para enseñarle al agente la estructura del mundo: quién depende de quién y cómo se relacionan las cosas.

```sql
-- =============================================
-- 🌐 CAPA ONTOLÓGICA: ¿QUIÉN ES QUIÉN?
-- =============================================

CREATE TABLE public.organizaciones (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE public.clientes (
    id BIGSERIAL PRIMARY KEY,
    organizacion_id BIGINT REFERENCES public.organizaciones(id), -- Relación de pertenencia
    tipo_cliente TEXT NOT NULL CHECK (tipo_cliente IN ('enterprise', 'pyme', 'individual'))
);

-- Le dejamos pistas semánticas al motor
COMMENT ON TABLE public.clientes IS 'Ontología: Entidad consumidora. Pertenece a una Organización matriz.';
```

💡 **Tip rápido:** Foreign Keys, taxonomías, o mapas tipo "X es filial de Y" = **Capa Ontológica**.

---

### 📌 3. CAPA VECTORIAL (Contexto Semántico Unstructured)

* **¿Dónde vive?:** Supabase (`pgvector`), Qdrant, Pinecone.
* **¿Qué archivo es?:** `03_capa_vectorial/vector_store_setup.sql` o tu script de ingesta RAG.
* **¿Para qué sirve?:** Para buscar cosas por "sentido" o "parecido", no por coincidencias exactas.

```sql
-- =============================================
-- 🔍 CAPA VECTORIAL: BÚSQUEDA POR SIMILITUD
-- =============================================

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE public.documentos_kb (
    id BIGSERIAL PRIMARY KEY,
    contenido TEXT NOT NULL,
    categoria_semantica TEXT, 
    pregunta_hipotetica TEXT,
    embedding VECTOR(1536) -- Búsqueda densa / embeddings
);
```

💡 **Tip rápido:** Dimensiones, `VECTOR(1536)`, chunking de PDFs o metadatos para RAG = **Capa Vectorial**.

---

### 📌 4. CAPA AGÉNTICA (Enrutamiento en Tiempo Real)

* **¿Dónde vive?:** En tu API (`FastAPI`, `LangGraph`).
* **¿Qué archivo es?:** `04_capa_agentica/agent_router.py`
* **¿Para qué sirve?:** Es el cerebro. Atrapa la pregunta del usuario y decide a cuál de las otras 3 capas enviarla.

```python
# =============================================
# 🤖 CAPA AGÉNTICA: EL TRAFICO Y LA DECISIÓN
# =============================================
from semantic_router import Route, RouteLayer
from semantic_router.encoders import OpenAIEncoder

# 1. Definimos las fronteras de intención
ruta_metrica = Route(
    name="CAPA_METRICA",
    utterances=["¿Cuál es el total de ventas netas?", "Dime el margen financiero"]
)

ruta_vectorial = Route(
    name="CAPA_VECTORIAL",
    utterances=["¿Cómo pido una devolución?", "Busca en los manuales de servicio"]
)

ruta_ontologica = Route(
    name="CAPA_ONTOLOGICA",
    utterances=["¿Qué clientes pertenecen a la Organización X?", "Muestra la estructura del grupo"]
)

# 2. Inicializamos el router (decisiones en <20ms)
encoder = OpenAIEncoder()
router = RouteLayer(encoder=encoder, routes=[ruta_metrica, ruta_vectorial, ruta_ontologica])

# 3. La orquestación
def orquestar_consulta(prompt_usuario: str):
    intencion = router(prompt_usuario)
    print(f"\n[🤖 Capa Agéntica] Intención: '{intencion.name}'")
    
    if intencion.name == "CAPA_METRICA":
        return "📊 Despachando a Cube.dev (Métrica)..."
    elif intencion.name == "CAPA_VECTORIAL":
        return "🔍 Despachando a Supabase pgvector (Vectorial)..."
    elif intencion.name == "CAPA_ONTOLOGICA":
        return "🌐 Despachando a Grafo/Relaciones (Ontológica)..."
    else:
        return "⚪ Respuestas generales del LLM..."
```

💡 **Tip rápido:** Clasificación de prompts, routers de latencia ultra baja o grafos de estado = **Capa Agéntica**.

---

## 🚨 La Trampa Mortal: *Layer Bleeding* (Solapamiento)

El error más común cuando la gente construye esto es mezclar las responsabilidades. Por ejemplo:

1. Usar la **Capa Vectorial** (RAG) para intentar responder preguntas ontológicas (ej. "adivinar" con embeddings qué empresa es filial de cuál en lugar de hacer un `JOIN`/Grafo).
2. Dejar que la **Capa Agéntica** intente calcular la matemática de las ventas directo en código de Python improvisado.

**Mantén cada capa en su casilla. Límites quirúrgicos = Sistema robusto.**

---

## 🚀 Inicio Rápido (Hands-on)

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/la-brujula-del-arquitecto.git
cd la-brujula-del-arquitecto
```

### 2. Probar la Capa Agéntica (Demo Interactiva)
```bash
# Crear un entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r 04_capa_agentica/requirements.txt

# Ejecutar el demo interactivo
python scripts/demo_orquestador.py
```

---

## 📜 Comunidad, Uso Educativo y Recomendaciones

¡Hola! 👋 Este repositorio es **100% educativo y abierto para la comunidad**. No vas a encontrar un contrato corporativo ni licencias frías aquí. Puedes usar, estudiar, modificar y compartir todo este conocimiento libremente en tus propios proyectos.

**¿Te sirvió esta arquitectura o te ayudó a estructurar tus agentes de IA?**
* ⭐ **Déjanos una estrella en GitHub:** Ayuda a que más desarrolladores descubran la regla de las 4 capas.
* 🗣️ **Deja tu recomendación / feedback:** Si tienes ideas, mejoras o comentarios sobre cómo te funcionó en producción, ¡abre un Issue o discusión!
* 📣 **Compártelo:** Pásaselo a tu equipo o compártelo en LinkedIn/X si crees que a alguien más le evitará dolores de cabeza.

