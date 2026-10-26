import tkinter as tk

mazes = [
    # 5 laberintos de 16x16 celdas (generados por DFS recursive backtracker)
    [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1],
        [1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
        [1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1],
        [1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1],
        [1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1],
        [1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1],
        [1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1],
        [1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1],
        [1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,1,0,0,2,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ],
    [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1],
        [1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1],
        [1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1],
        [1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1],
        [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1],
        [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1],
        [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,2,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ],
    [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1],
        [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1],
        [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1],
        [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1],
        [1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1],
        [1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1],
        [1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1],
        [1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
        [1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,1],
        [1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,2,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ],
    [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1],
        [1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
        [1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1],
        [1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,2,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ],
    [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1],
        [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1],
        [1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1],
        [1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1],
        [1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1],
        [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1],
        [1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1],
        [1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1],
        [1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1],
        [1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,2,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ],
]

CELL_SIZE = 25
player_pos = [1, 1]
level = 0
time_limit = 30
time_left = time_limit
game_finished = False
after_id = None  # ID del temporizador activo
time_text_id = None  # ID del texto del temporizador

def draw_maze(canvas):
    canvas.delete("all")
    if level >= len(mazes):
        return
    maze = mazes[level]
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            cell = maze[y][x]
            color = "black" if cell == 1 else "white"
            if cell == 2:
                color = "gold"
            canvas.create_rectangle(
                x * CELL_SIZE, y * CELL_SIZE,
                (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                fill=color
            )
    px, py = player_pos
    margin = max(3, CELL_SIZE // 8)
    canvas.create_oval(
        px * CELL_SIZE + margin, py * CELL_SIZE + margin,
        (px + 1) * CELL_SIZE - margin, (py + 1) * CELL_SIZE - margin,
        fill="blue"
    )
    global time_text_id
    time_text_id = canvas.create_text(350, 12, text=f"Tiempo: {time_left}", font=("Arial", 11), fill="red")
    canvas.create_text(60, 12, text=f"Nivel: {level + 1}", font=("Arial", 11), fill="blue")

def move(dx, dy):
    global level, player_pos, game_finished
    if game_finished or level >= len(mazes):
        return
    maze = mazes[level]
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy
    if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
        if maze[new_y][new_x] != 1:
            player_pos[0] = new_x
            player_pos[1] = new_y
            draw_maze(canvas)
            if maze[new_y][new_x] == 2:
                level += 1
                if level < len(mazes):
                    start_level()
                else:
                    canvas.create_text(200, 190, text="¡Ganaste todos los niveles!", font=("Arial", 16), fill="green")
                    canvas.create_text(200, 220, text="Pulsa R para reiniciar", font=("Arial", 11), fill="gray")
                    game_finished = True
                    cancel_timer()

def start_level():
    global player_pos, time_left
    player_pos = [1, 1]
    time_left = time_limit
    draw_maze(canvas)
    cancel_timer()
    countdown()

def update_time_text():
    if time_text_id is not None:
        canvas.itemconfig(time_text_id, text=f"Tiempo: {time_left}")

def countdown():
    global time_left, game_finished, after_id
    if game_finished or level >= len(mazes):
        return
    if time_left > 0:
        time_left -= 1
        update_time_text()
        after_id = root.after(1000, countdown)
    else:
        canvas.create_text(200, 190, text="¡Tiempo agotado!", font=("Arial", 16), fill="red")
        canvas.create_text(200, 220, text="Pulsa R para reiniciar", font=("Arial", 11), fill="gray")
        game_finished = True
        cancel_timer()

def cancel_timer():
    global after_id
    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None

def restart():
    global level, player_pos, time_left, game_finished
    cancel_timer()
    level = 0
    player_pos = [1, 1]
    time_left = time_limit
    game_finished = False
    start_level()

root = tk.Tk()
root.title("Laberinto por Niveles V2.1 (16x16)")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.bind("<Up>", lambda e: move(0, -1))
root.bind("<Down>", lambda e: move(0, 1))
root.bind("<Left>", lambda e: move(-1, 0))
root.bind("<Right>", lambda e: move(1, 0))
root.bind("<r>", lambda e: restart())
root.bind("<R>", lambda e: restart())

start_level()
root.mainloop()