#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
🧭 DEMO INTERACTIVA: ORQUESTADOR DE LA BRÚJULA DEL ARQUITECTO
==============================================================================
Este script permite probar interactivamente el enrutamiento de intenciones
entre las 4 capas de arquitectura para Agentes de IA.
"""

import sys
import os
import importlib.util

# Forzar codificación utf-8 para la salida en consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# Importar dinámicamente AgenticRouter desde 04_capa_agentica/agent_router.py
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "04_capa_agentica", "agent_router.py"))
spec = importlib.util.spec_from_file_location("agent_router", module_path)
agent_router_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent_router_mod)

AgenticRouter = agent_router_mod.AgenticRouter


def banner():
    print("=" * 75)
    print("🧭 LA BRÚJULA DEL ARQUITECTO - SIMULADOR INTERACTIVO DE CAPAS DE AGENTE")
    print("=" * 75)
    print("Escribe una pregunta para ver a qué capa es despachada en tiempo real.")
    print("Escribe 'salir' o 'exit' para terminar.\n")


def main():
    banner()
    router = AgenticRouter()

    while True:
        try:
            prompt = input("\n💬 Tu pregunta > ").strip()
            if not prompt:
                continue

            if prompt.lower() in ["salir", "exit", "quit"]:
                print("\n👋 ¡Hasta luego! Mantén las capas bien separadas.")
                break

            res = router.orquestar(prompt)
            print("-" * 60)
            print(f"🎯 Prompt            : {res['prompt']}")
            print(f"🏷️  Intención        : {res['intencion']}")
            print(f"🏛️  Capa Asignada    : {res['capa']}")
            print(f"⚙️  Motor            : {res['motor']}")
            print(f"📄 Archivo de Reglas : {res['archivo_origen']}")
            print(f"📌 Acción Executed   : {res['accion']}")
            print("-" * 60)

        except (KeyboardInterrupt, EOFError):
            print("\n👋 Sesión finalizada.")
            break


if __name__ == "__main__":
    main()
