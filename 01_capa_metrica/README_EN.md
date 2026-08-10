# 📊 Metric Layer (Deterministic Numerical Rules)

> **Design Signature:** Pure business math and rule files (`YAML` / `Cube.dev` / `dbt`).

---

## 🎯 Purpose of the Metric Layer
Ensure that **business mathematical formulas are immutable and deterministic**.

Large Language Models (LLMs) are probabilistic text generators, **not calculators**. Asking an LLM to generate raw on-the-fly SQL queries like `SUM(monto - descuento)` leads inevitably to hallucinations and inconsistent reporting across dashboards.

This layer serves as the **Single Source of Truth (SSOT)** for business metrics.

---

## 🛠️ Typical Stack
* [Cube.dev](https://cube.dev/) (Decoupled Semantic Layer)
* `dbt` (Data Build Tool - Semantic Layer)
* Looker LookML

---

## 💡 Golden Rules
1. **Zero mathematical logic in prompts:** NEVER ask the LLM to "calculate margins". Ask it to query the Metric Layer instead.
2. **Immutable definitions:** If "Net Sales" requires filtering by `estado = 'completada'`, that logic belongs in the `.yml` file, not in system prompts.
3. **Clear signatures:** When you spot a `.yml` file with `measures` and `dimensions`, you are looking at the **Metric Layer**.

---

## 📂 Files in this section
* [`model/cubes/Ventas.yml`](model/cubes/Ventas.yml): Complete semantic definition example in Cube.dev.
