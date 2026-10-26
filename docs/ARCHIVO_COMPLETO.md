# Documentación Técnica — Juego del Laberinto

Esta documentación explica la arquitectura, el modelo de datos, la lógica de ejecución y las diferencias técnicas entre las cuatro versiones del proyecto: `laberintoV10.py`, `laberintoV11.py`, `laberintoV20.py` y `laberintoV21.py`.

---

## 1. Descripción General

El proyecto es un videojuego 2D por cuadrícula desarrollado en **Python** utilizando **Tkinter** como biblioteca de interfaz gráfica. El jugador controla una ficha en un tablero y debe encontrar el camino hacia la casilla de meta antes de que expire el temporizador del nivel. Consta de **5 niveles** en todas las versiones.

Las cuatro versiones comparten la misma interfaz, el mismo tamaño de ventana y la misma lógica de juego. La evolución consiste en:
1. **V10 → V11:** correcciones de usabilidad (color de la meta, reinicio, parpadeo).
2. **V11 → V20 → V21:** más celdas dentro del mismo lienzo, es decir, laberintos más complejos sin ocupar más pantalla.

---

## 2. Especificación Técnica y Requisitos

| Parámetro | V10 | V11 | V20 | V21 |
| --- | --- | --- | --- | --- |
| **Lenguaje** | Python 3.x | Python 3.x | Python 3.x | Python 3.x |
| **Librería gráfica** | `tkinter` | `tkinter` | `tkinter` | `tkinter` |
| **Grilla** | 8×8 | 8×8 | 10×10 | 16×16 |
| **Tamaño de celda** | 50 px | 50 px | 40 px | 25 px |
| **Lienzo (canvas)** | 400×400 px | 400×400 px | 400×400 px | 400×400 px |
| **Tiempo por nivel** | 20 s | 20 s | 20 s | 30 s |

La fórmula que mantiene constante el lienzo es:

```text
celdas × CELL_SIZE = 400 px
   8 × 50 = 400
  10 × 40 = 400
  16 × 25 = 400
```

- **Resolución de pantalla requerida (las 4 versiones):** mínimo **480×480 píxeles**, para alojar la ventana completa con su barra de título, marcos y bordes nativos del sistema operativo.

---

## 3. Modelo de Datos y Constantes

### 3.1 Estructura de la Matriz del Laberinto (`mazes`)

Cada nivel es una matriz bidimensional (lista de listas) de enteros. Las dimensiones cambian por versión:

```python
mazes = [
    # V10 / V11: nivel de 8×8
    [
        [1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,1],
        ...
    ],
    # V20: nivel de 10×10 — V21: nivel de 16×16
    ...
]
```

#### Codificación de Celdas
- **`1` — Pared:** celda infranqueable (color negro).
- **`0` — Camino libre:** celda transitable (color blanco).
- **`2` — Meta:** celda de llegada (azul en V10, dorado en V11/V20/V21).

#### Origen de los laberintos
- **V10, V11, V20:** matrices escritas a mano.
- **V21:** matrices generadas con el algoritmo **DFS recursive backtracker** (generación perfecta de laberintos: exactamente un camino entre dos celdas cualesquiera), con semilla fija para reproducibilidad. Las matrices resultantes quedaron embebidas en el archivo: el script no genera nada en tiempo de ejecución ni depende de `random`.

### 3.2 Variables de Estado Global

| Variable | Tipo | Descripción |
| --- | --- | --- |
| `CELL_SIZE` | `int` | Tamaño en píxeles de cada celda (50 / 50 / 40 / 25 según versión). |
| `player_pos` | `list[int]` | Coordenadas del jugador `[x, y]` en el tablero. Posición inicial: `[1, 1]`. |
| `level` | `int` | Índice del nivel actual (`0` a `4`). |
| `time_limit` | `int` | Tiempo límite por nivel en segundos (20, salvo 30 en V21). |
| `time_left` | `int` | Tiempo restante en el nivel. |
| `game_finished` | `bool` | Flag que indica si el juego ha finalizado (victoria o derrota). |
| `after_id` | `str \| None` | Identificador del evento `after` activo de Tkinter para cancelar el temporizador. |
| `time_text_id` | `int \| None` | *(V11 en adelante)* Identificador del elemento de texto del tiempo, para actualizarlo de forma atómica. |

---

## 4. Funciones Principales

### `draw_maze(canvas)`
Dibuja el estado completo del nivel actual:
1. Borra el contenido del lienzo (`canvas.delete("all")`).
2. Dibuja las celdas del tablero (rectángulos) según la matriz del nivel actual.
3. Dibuja al jugador como un óvalo azul centrado en su celda activa. El margen interior del óvalo es fijo en V10/V11 (10 px) y proporcional en V20 (6 px) y V21 (`CELL_SIZE // 8`, con mínimo 3 px).
4. Renderiza los textos de **Nivel** y **Tiempo restante**, y guarda el identificador del texto del tiempo en `time_text_id` (V11 en adelante).

### `move(dx, dy)`
Gestiona el desplazamiento del jugador:
1. Comprueba si el juego está activo (`not game_finished`).
2. Calcula la nueva posición proyectada: `new_x = x + dx`, `new_y = y + dy`.
3. Valida límites del tablero contra `len(maze)` y `len(maze[0])`, lo que hace que la función sirva igual para 8×8, 10×10 o 16×16 sin cambios.
4. Valida colisiones: solo permite mover si la celda destino no es pared (`!= 1`).
5. Actualiza la posición del jugador y redibuja la pantalla.
6. **Detector de victoria:** si la celda destino es `2` (Meta):
   - Si quedan más niveles: incrementa `level` y ejecuta `start_level()`.
   - Si era el último nivel: muestra el mensaje de victoria y el aviso de reinicio (V11+), marca `game_finished = True` y cancela el temporizador.

### `start_level()`
Inicia un nuevo nivel:
1. Reestablece la posición del jugador a `[1, 1]`.
2. Reestablece el contador de tiempo a `time_limit`.
3. Ejecuta `draw_maze()` para pintar el nuevo escenario.
4. Cancela cualquier temporizador previo y arranca la cuenta regresiva (`countdown()`).

### `update_time_text()` *(V11 en adelante)*
Actualiza únicamente el texto del temporizador con `canvas.itemconfig(time_text_id, ...)`, sin redibujar el laberinto. Es la corrección del parpadeo de V10.

### `countdown()`
Bucle del temporizador basado en el evento `root.after(1000, countdown)`:
- Si `time_left > 0`: decrementa `time_left` en 1, refresca el texto (V11+) o el canvas completo (V10) y programa la siguiente ejecución en 1000 ms.
- Si `time_left == 0`: detiene el juego, muestra "¡Tiempo agotado!" (y en V11+ el aviso de reinicio) y cancela el ciclo.

### `cancel_timer()`
Cancela de forma segura la llamada programada con `root.after_cancel(after_id)` para evitar ejecuciones concurrentes o desbordamientos al reiniciar o cambiar de nivel.

### `restart()` *(V11 en adelante)*
Reinicia la partida completa desde el nivel 1: cancela el temporizador, restablece `level = 0`, `player_pos = [1, 1]`, `time_left = time_limit`, `game_finished = False` y ejecuta `start_level()`.

---

## 5. Eventos y Mapeo de Teclado

```python
root.bind("<Up>", lambda e: move(0, -1))
root.bind("<Down>", lambda e: move(0, 1))
root.bind("<Left>", lambda e: move(-1, 0))
root.bind("<Right>", lambda e: move(1, 0))

# V11, V20 y V21:
root.bind("<r>", lambda e: restart())
root.bind("<R>", lambda e: restart())
```

---

## 6. Cuadro Comparativo de Versiones

| Característica | V10 | V11 | V20 | V21 |
| --- | --- | --- | --- | --- |
| **Grilla** | 8×8 | 8×8 | 10×10 | 16×16 |
| **`CELL_SIZE`** | 50 px | 50 px | 40 px | 25 px |
| **Lienzo** | 400×400 | 400×400 | 400×400 | 400×400 |
| **Tiempo por nivel** | 20 s | 20 s | 20 s | 30 s |
| **Color de la meta** | Azul (igual al jugador) | Dorado | Dorado | Dorado |
| **Reinicio con `R`** | No | Sí | Sí | Sí |
| **Actualización del tiempo** | Redibuja todo el canvas | `itemconfig` solo al texto | Ídem V11 | Ídem V11 |
| **Celdas de paso (mín./máx.)** | 4–10 | 4–10 | 13–16 | 32–72 |
| **Origen de los laberintos** | Manuales | Manuales | Manuales | Algoritmo DFS |

---

## 7. Análisis de Resolubilidad de los Niveles

Todos los niveles de las cuatro versiones fueron verificados algorítmicamente mediante **Búsqueda en Anchura (BFS)** desde `(1, 1)` hasta la meta, y mediante una **simulación completa de partida** que recorre los 5 niveles disparando la victoria.

### V10 y V11 (8×8)
| Nivel | Meta | Distancia mínima |
| --- | --- | --- |
| 1 | `(6, 6)` | 10 pasos |
| 2 | `(5, 3)` | 6 pasos |
| 3 | `(3, 3)` | 4 pasos |
| 4 | `(5, 3)` | 6 pasos |
| 5 | `(3, 3)` | 4 pasos |

### V20 (10×10)
| Nivel | Meta | Distancia mínima |
| --- | --- | --- |
| 1 | `(8, 7)` | 13 pasos |
| 2 | `(8, 8)` | 14 pasos |
| 3 | `(8, 8)` | 16 pasos |
| 4 | `(8, 8)` | 14 pasos |
| 5 | `(8, 8)` | 14 pasos |

### V21 (16×16)
| Nivel | Meta | Distancia mínima |
| --- | --- | --- |
| 1 | `(13, 13)` | 72 pasos |
| 2 | `(13, 13)` | 60 pasos |
| 3 | `(13, 13)` | 32 pasos |
| 4 | `(13, 13)` | 32 pasos |
| 5 | `(13, 13)` | 56 pasos |

El salto de dificultad entre V20 y V21 (de ~14 a ~50 pasos de media) es lo que obligó a subir el tiempo por nivel de 20 a 30 segundos.

---

## 8. Instrucciones de Ejecución

```bash
# Versión original
python laberintoV10.py

# Versión corregida (8×8)
python laberintoV11.py

# Versión intermedia (10×10)
python laberintoV20.py

# Versión más compleja (16×16)
python laberintoV21.py
```

---

## 9. Verificación Automatizada

Comprobaciones que se han ejecutado sobre el código:

```bash
# Compilación sin errores de sintaxis (las 4 versiones)
python -m py_compile laberintoV10.py laberintoV11.py laberintoV20.py laberintoV21.py
```

Además, la lógica de juego se prueba sin interfaz gráfica sustituyendo el canvas por un objeto simulado (doble) y recorriendo los niveles con la ruta BFS:

```python
import laberintoV21 as L

class D: pass                      # canvas simulado
L.canvas = D()
L.canvas.delete = lambda *a: None
L.canvas.create_rectangle = lambda *a, **k: None
L.canvas.create_oval = lambda *a, **k: None
L.canvas.create_text = lambda *a, **k: 1
L.canvas.itemconfig = lambda *a, **k: None
# ... navegar los 5 niveles con move() hasta game_finished == True
```

---

## 10. Limitaciones Conocidas

- **Sin tests automatizados persistentes:** las verificaciones de resolubilidad se hicieron con scripts auxiliares desechables, no con una suite versionada.
- **`game_finished` no bloquea la victoria parcial:** al ganar, el nivel queda en `len(mazes)`; cualquier posterior pulsación de flecha se ignora por la guarda de `move()`.
- **Estado global:** el juego usa variables globales en lugar de una clase de estado, lo que dificulta añadir más de una partida simultánea o tests unitarios puros.
- **Colisión por celda:** el jugador se mueve de centro en centro; no hay desplazamiento suave ni animación.