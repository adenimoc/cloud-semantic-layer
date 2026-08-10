# 📊 Capa Métrica (Reglas Numéricas Deterministas)

> **Firma de diseño:** Archivos de reglas y matemática pura (`YAML` / `Cube.dev` / `dbt`).

---

## 🎯 Objetivo de la Capa Métrica
Garantizar que **la matemática del negocio sea inmutable y determinista**. 

Los Modelos de Lenguaje (LLMs) son generadores de texto probabilísticos, **no calculadoras**. Pedirle a un LLM que escriba una consulta SQL improvisada con un `SUM(monto - descuento)` en caliente conduce inevitablemente a hallucination (alucinaciones) y métricas inconsistentes en los reportes ejecutivos.

En esta capa se declara la **Verdad Única del Negocio (Single Source of Truth)**.

---

## 🛠️ Herramientas Típicas
* [Cube.dev](https://cube.dev/) (Capa semántica desacoplada)
* `dbt` (Data Build Tool - Semantic Layer)
* Looker LookML

---

## 💡 Reglas de Oro
1. **Cero lógica matemática en prompts:** NUNCA le pidas al LLM que "calcule el margen". Pídele que genere una consulta hacia la Capa Métrica.
2. **Definiciones inmutables:** Si "Ventas Netas" requiere filtrar `estado = 'completada'`, esa regla vive en el archivo `.yml`, no en el prompt del sistema.
3. **Firmas claras:** Cuando veas un archivo `.yml` con `measures` y `dimensions`, estás parado en la **Capa Métrica**.

---

## 📂 Archivos en esta sección
* [`model/cubes/Ventas.yml`](model/cubes/Ventas.yml): Ejemplo completo de definición semántica en Cube.dev.
