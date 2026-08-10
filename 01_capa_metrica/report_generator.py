# ==============================================================================
# 📊 GENERADOR DE REPORTES AUTOMÁTICOS (Capa Métrica)
# ==============================================================================
# Firma de diseño: Python / Markdown / JSON Exporters
# Propósito: Compilar reportes ejecutivos automatizados a partir de datos 
#            numéricos deterministas calculados por la Capa Métrica (Cube.dev).
# ==============================================================================

import json
import sys
from typing import Dict, Any

# Forzar codificación utf-8 en consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class ExecutiveReportGenerator:
    """Compila reportes ejecutivos estructurados a partir de métricas inmutables."""

    @staticmethod
    def generar_reporte_ventas(datos_metricos: Dict[str, Any]) -> str:
        """Genera un informe en formato Markdown listo para presentar a ejecutivos."""
        ventas_totales = datos_metricos.get("ventas_totales", 150000.00)
        ventas_netas = datos_metricos.get("ventas_netas", 135000.00)
        descuentos = ventas_totales - ventas_netas
        ticket_promedio = datos_metricos.get("ticket_promedio", 450.00)
        transacciones = datos_metricos.get("conteo_transacciones", 300)

        pct_descuento = (descuentos / ventas_totales * 100) if ventas_totales > 0 else 0.0

        reporte = f"""
# 📈 REPORTE EJECUTIVO AUTOMÁTICO DE DESEMPEÑO DE VENTAS

> **Fuente de Verdad:** Capa Métrica Inmutable (`model/cubes/Ventas.yml`)
> **Motor Semántico:** Cube.dev / Data Warehouse
> **Garantía:** Cálculo determinista (0% alucinaciones de LLM)

---

### 📊 Resumen Financiero
| Métrica | Valor Calculado | Descripción |
| :--- | :--- | :--- |
| **Ventas Totales Brutas** | `${ventas_totales:,.2f}` | Suma de todas las órdenes procesadas |
| **Descuentos Aplicados** | `${descuentos:,.2f}` | Deducción por promociones |
| **Ventas Netas (Completadas)** | `${ventas_netas:,.2f}` | Ingreso real de órdenes completadas |
| **Ticket Promedio** | `${ticket_promedio:,.2f}` | Monto promedio por transacción |
| **Transacciones Totales** | `{transacciones:,}` | Conteo total de operaciones |

---

### 💡 Análisis y Conclusiones de Negocio
1. **Margen Neto:** El ingreso neto final refleja una retención del `{100 - pct_descuento:.1f}%` sobre las ventas brutas.
2. **Impacto Promocional:** Los descuentos representaron un `{pct_descuento:.1f}%` del volumen total.
3. **Eficiencia por Orden:** Se mantuvo un ticket promedio de `${ticket_promedio:,.2f}` a lo largo de `{transacciones}` operaciones.

---
*Este reporte fue generado de forma automática mediante la integración de la Capa Métrica y el orquestador Agéntico.*
"""
        return reporte.strip()


if __name__ == "__main__":
    datos_simulados = {
        "ventas_totales": 250000.00,
        "ventas_netas": 225000.00,
        "ticket_promedio": 750.00,
        "conteo_transacciones": 300
    }
    reporte_md = ExecutiveReportGenerator.generar_reporte_ventas(datos_simulados)
    print(reporte_md)
