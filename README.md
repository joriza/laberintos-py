# Laberinto por Niveles

Juego de laberinto de 5 niveles escrito en **Python** con la librería **Tkinter**.
Cada nivel debe resolverse antes de que se agote el tiempo.

Todas las versiones ocupan **exactamente la misma pantalla (canvas de 400×400 px)**; lo que cambia es el tamaño de la cuadrícula y, por tanto, la complejidad del laberinto.

## Contenido

| Archivo | Grilla | Celda | Tiempo/nivel | Descripción |
| --- | --- | --- | --- | --- |
| `laberintoV10.py` | 8×8 | 50 px | 20 s | Versión original (meta azul, sin reinicio). |
| `laberintoV11.py` | 8×8 | 50 px | 20 s | Versión mejorada (meta dorada, tecla `R`, sin parpadeo). |
| `laberintoV20.py` | 10×10 | 40 px | 20 s | Laberintos más complejos, mismo tamaño de ventana. |
| `laberintoV21.py` | 16×16 | 25 px | 30 s | Laberintos generados por algoritmo DFS, máxima complejidad. |

### Documentación

| Archivo | Ubicación | Contenido |
| --- | --- | --- |
| `README.md` | Raíz del proyecto | Este documento (guía de uso y versiones). |
| `docs/ARCHIVO_COMPLETO.md` | `docs/` | Documentación técnica detallada del código. |
| `pdt-laberinto.md` | Raíz del proyecto | Apunte personal del dueño. **No es documentación del proyecto ni especificación.** |

## Requisitos

- Python 3.x (se ha verificado con Python 3.14).
- Tkinter (incluido en la distribución estándar de Python en Windows, Linux y macOS).
- Pantalla con una resolución mínima de **480×480 píxeles** (el canvas del juego mide 400×400 en todas las versiones y la suma de bordes y barra de título de la ventana añade unos 40–80 píxeles).

## Cómo jugar

1. Abre cualquiera de las versiones con Python:
   ```bash
   python laberintoV21.py
   ```
2. Usa las **flechas del teclado** para moverte:
   - `↑` / `↓` / `←` / `→` — desplazamiento en las cuatro direcciones.
3. Llega a la **meta** (cuadrado dorado, o azul en V10) antes de que se agote el tiempo.
4. Al pasar la meta avanzas automáticamente al siguiente nivel. Al resolver los 5 niveles gana el juego.
5. Si se agota el tiempo, el juego termina. Desde **V11** en adelante puedes pulsar **`R`** para reiniciar desde el nivel 1 sin cerrar la ventana.

## Reglas del tablero

Cada laberinto es una matriz de celdas (8×8, 10×10 o 16×16 según la versión) donde:

| Valor | Significado | Color en pantalla |
| --- | --- | --- |
| `1` | Pared (bloqueo) | Negro |
| `0` | Camino libre | Blanco |
| `2` | Meta | Azul (V10) / Dorado (V11, V20, V21) |

El jugador empieza en la celda `(1, 1)` (fila 1, columna 1) de cada nivel, siempre dentro del borde de paredes.

## Estado del proyecto

- ✅ Compilación limpia (`python -m py_compile` sin errores) en las **4 versiones**.
- ✅ Los 5 niveles de cada versión son solucionables (verificado con BFS desde el inicio hasta la meta).
- ✅ El inicio de cada nivel es siempre una celda de camino (`0`).
- ✅ Simulación completa de juego: se recorren los 5 niveles de cada versión hasta disparar la victoria.

## Notas de versión

### V10 → V11 (correcciones de bajo costo)

1. **Meta en dorado** en lugar de azul, para no confundirla con el jugador (ambos eran azules).
2. **Tecla `R` para reiniciar** el juego completo desde el nivel 1, sin tener que cerrar la ventana.
3. **Temporizador sin parpadeo**: en V10 el canvas se redibujaba completo cada segundo; en V11 solo se actualiza el texto del tiempo con `canvas.itemconfig`.

### V11 → V20 (más complejidad, misma pantalla)

- Cuadrícula ampliada de **8×8 a 10×10** reduciendo la celda de 50 px a **40 px**.
- Laberintos rediseñados con pasillos más largos y más callejones sin salida.
- El lienzo sigue midiendo **400×400 px**: la ventana no crece.

### V20 → V21 (máxima complejidad, misma pantalla)

- Cuadrícula ampliada de **10×10 a 16×16** reduciendo la celda de 40 px a **25 px**.
- Laberintos **generados algorítmicamente** con DFS recursive backtracker: caminos serpenteantes de verdad, sin tramos rectos largos.
- Tiempo por nivel elevado de 20 s a **30 s** porque el camino mínimo sube de ~16 a **32–72 pasos**.
- Lienzo de **400×400 px** idéntico a las versiones anteriores.