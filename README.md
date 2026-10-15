# Ecuaciones-actividad-semana9

Ejercicios de la Unidad 3 (Pruebas automatizadas) del curso **Construcción de Software** — Semana 9.

## Contenido

| Archivo | Descripción |
| --- | --- |
| `calculadora.py` | Funciones puras de una calculadora básica (suma, resta, multiplicación, división). |
| `test_calculadora.py` | Pruebas unitarias de la calculadora con `unittest` (incluye validación de división entre cero). |
| `ecuacion.py` | Resolvedor de ecuaciones cuadráticas `ax² + bx + c = 0` según el discriminante. |
| `test_ecuacion.py` | Pruebas unitarias del resolvedor, usando `assertEqual`, `assertAlmostEqual`, `assertRaises` y `subTest`. |

## Cómo ejecutar las pruebas

\`\`\`bash
python -m unittest test_calculadora -v
python -m unittest test_ecuacion -v
\`\`\`

O para correr todas a la vez desde la carpeta del proyecto:

\`\`\`bash
python -m unittest discover -v
\`\`\`

## Casos cubiertos en `test_ecuacion.py`

- Dos soluciones reales distintas (discriminante > 0)
- Una solución real / raíz doble (discriminante = 0)
- Sin solución real (discriminante < 0)
- Caso lineal (a = 0, b ≠ 0)
- Coeficientes inválidos (a = 0, b = 0) → `ValueError`
- Casos parametrizados con `subTest`
- Coeficientes grandes
- Precisión decimal (`places=10`)
- Coeficiente `c` = 0
- Coeficiente `a` negativo
- Todos los coeficientes en cero → `ValueError`

## Equipo

- Oscar — Desarrollador principal / Líder de proyecto
- Diego — Revisor de código / Documentador

## Docente

Ing. Henderson Nozart Gibaja Reyes
