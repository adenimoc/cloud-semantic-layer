# ==============================================================================
# 🤖 CAPA AGÉNTICA: EL TRÁFICO Y LA DECISIÓN DE ENRUTAMIENTO
# ==============================================================================
# Firma de diseño: Python / Routers de intenciones / Orquestadores
# Propósito: Evaluar el prompt del usuario en tiempo real y enviarlo a la capa correcta.
# Regla de Oro: El router toma decisiones en latencia ultra-baja (<20ms).
# ==============================================================================

import os
import sys
from typing import Dict, Any

# Intentamos importar semantic_router si está disponible
try:
    from semantic_router import Route, RouteLayer
    from semantic_router.encoders import OpenAIEncoder
    SEMANTIC_ROUTER_AVAILABLE = True
except ImportError:
    SEMANTIC_ROUTER_AVAILABLE = False


# 1. Definimos las fronteras de intención (Routes)
RUTAS_DEFINICION = [
    {
        "name": "CAPA_METRICA",
        "description": "Consultas sobre cálculos numéricos, agregaciones, sumas, ventas netas y métricas de negocio.",
        "utterances": [
            "¿Cuál es el total de ventas netas?",
            "Dime el margen financiero del último mes",
            "¿Cuál es el ticket promedio de compra?",
            "Calcula el total transaccionado",
            "Muéstrame el reporte de ventas por estado"
        ]
    },
    {
        "name": "CAPA_VECTORIAL",
        "description": "Consultas sobre manuales, políticas de reembolso, documentación no estructurada y guías.",
        "utterances": [
            "¿Cómo pido una devolución de un producto?",
            "Busca en los manuales de servicio la sección de garantías",
            "¿Cuáles son las políticas de envío internacional?",
            "¿Qué dice el documento sobre la cancelación de cuenta?",
            "Explícame los pasos para soporte técnico"
        ]
    },
    {
        "name": "CAPA_ONTOLOGICA",
        "description": "Consultas sobre relaciones entre entidades, pertenencia de clientes, taxonomías y jerarquías.",
        "utterances": [
            "¿Qué clientes pertenecen a la Organización X?",
            "Muestra la estructura jerárquica del grupo corporativo",
            "¿De qué organización es filial la empresa Y?",
            "Lista todos los clientes registrados bajo una entidad matriz",
            "¿Quién es el contacto principal de la organización Z?"
        ]
    }
]


class AgenticRouter:
    """Orquestador de la Capa Agéntica que clasifica intenciones y despacha a la capa adecuada."""

    def __init__(self, use_openai: bool = False):
        self.use_openai = use_openai and os.getenv("OPENAI_API_KEY") is not None
        self.router = None

        if self.use_openai and SEMANTIC_ROUTER_AVAILABLE:
            try:
                routes = [
                    Route(name=r["name"], utterances=r["utterances"])
                    for r in RUTAS_DEFINICION
                ]
                encoder = OpenAIEncoder()
                self.router = RouteLayer(encoder=encoder, routes=routes)
                print("⚡ [Capa Agéntica] SemanticRouter inicializado con OpenAI.")
            except Exception as e:
                print(f"⚠️ [Capa Agéntica] Fallback a router heurístico: {e}")
                self.use_openai = False
        else:
            print("ℹ️ [Capa Agéntica] Modo heurístico local (sin API Key / Fallback activo).")

    def clasificar_intencion(self, prompt: str) -> str:
        """Clasifica el prompt del usuario en una de las 4 capas de arquitectura."""
        prompt_lower = prompt.lower()

        # Si tenemos SemanticRouter configurado con OpenAI
        if self.router:
            resultado = self.router(prompt)
            if resultado and resultado.name:
                return resultado.name

        # Fallback Heurístico local (palabras clave / semántica básica para demos)
        metrica_keywords = ["ventas", "total", "netas", "margen", "ticket", "calcula", "monto", "promedio"]
        vectorial_keywords = ["devolución", "manual", "política", "garantía", "pasos", "soporte", "documento", "envío"]
        ontologica_keywords = ["pertenecen", "organización", "jerarquía", "filial", "estructura", "entidad", "grupo"]

        if any(kw in prompt_lower for kw in metrica_keywords):
            return "CAPA_METRICA"
        elif any(kw in prompt_lower for kw in vectorial_keywords):
            return "CAPA_VECTORIAL"
        elif any(kw in prompt_lower for kw in ontologica_keywords):
            return "CAPA_ONTOLOGICA"
        else:
            return "CAPA_GENERAL_LLM"

    def orquestar(self, prompt_usuario: str) -> Dict[str, Any]:
        """Procesa la consulta y la despacha al subsistema correspondiente."""
        intencion = self.clasificar_intencion(prompt_usuario)
        
        despacho_map = {
            "CAPA_METRICA": {
                "capa": "📊 Capa Métrica",
                "motor": "Cube.dev / Semantic Layer",
                "archivo_origen": "01_capa_metrica/model/cubes/Ventas.yml",
                "accion": "Ejecutando consulta SQL inmutable en Cube.dev (sin alucinaciones numéricas)..."
            },
            "CAPA_VECTORIAL": {
                "capa": "🔍 Capa Vectorial",
                "motor": "Supabase pgvector / Vector Store",
                "archivo_origen": "03_capa_vectorial/vector_store_setup.sql",
                "accion": "Buscando contexto relevante por similitud de coseno en la Base de Conocimientos..."
            },
            "CAPA_ONTOLOGICA": {
                "capa": "🌐 Capa Ontológica",
                "motor": "Postgres Relacional / Motor de Grafos",
                "archivo_origen": "02_capa_ontologica/schema_ontologia.sql",
                "accion": "Navegando relaciones estáticas y claves foráneas en la jerarquía de entidades..."
            },
            "CAPA_GENERAL_LLM": {
                "capa": "⚪ Respuestas Generales",
                "motor": "LLM estándar",
                "archivo_origen": "N/A",
                "accion": "Generando respuesta conversacional directa del modelo de lenguaje..."
            }
        }

        info = despacho_map.get(intencion, despacho_map["CAPA_GENERAL_LLM"])
        return {
            "prompt": prompt_usuario,
            "intencion": intencion,
            "capa": info["capa"],
            "motor": info["motor"],
            "archivo_origen": info["archivo_origen"],
            "accion": info["accion"]
        }


if __name__ == "__main__":
    router = AgenticRouter()
    prompts_prueba = [
        "¿Cuál es el total de ventas netas de este mes?",
        "¿Cómo pido una devolución de un artículo dañado?",
        "¿Qué clientes pertenecen a la Organización Alpha?",
        "Hola, ¿puedes contarme un chiste sobre código?"
    ]

    print("\n--- 🤖 PRUEBA DE ENRUTAMIENTO AGÉNTICO ---")
    for prompt in prompts_prueba:
        res = router.orquestar(prompt)
        print(f"\nUser Prompt: \"{res['prompt']}\"")
        print(f" -> Intención Detectada : {res['intencion']}")
        print(f" -> Capa Asignada       : {res['capa']}")
        print(f" -> Motor de Destino    : {res['motor']}")
        print(f" -> Archivo de Reglas   : {res['archivo_origen']}")
        print(f" -> Acción              : {res['accion']}")
