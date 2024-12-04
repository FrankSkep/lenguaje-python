import customtkinter as ctk
import tkinter.messagebox as messagebox
import random
import time

class SlidingPuzzle:
    def __init__(self, root, size=4):
        self.root = root
        self.size = size
        self.tiles = []
        self.empty_tile = (size - 1, size - 1)
        self.grid = [[(i * size + j + 1) % (size * size)
                      for j in range(size)] for i in range(size)]
        self.attempts = 0
        self.attempts_var = ctk.StringVar(value=f"Movimientos: {self.attempts}")
        self.start_time = time.time()
        self.timer_running = True
        self.time_var = ctk.StringVar(value="fTiempo: 0s")
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Sliding Puzzle")
        self.center_window(self.root, 500, 620)

        # Título decorativo
        title_frame = ctk.CTkFrame(self.root, height=50, width=400)
        title_frame.pack(pady=(10, 20))
        title_label = ctk.CTkLabel(
            title_frame, text="¡Desliza y Gana!", font=("Arial", 20, "bold"), anchor="center"
        )
        title_label.pack(fill="both", expand=True)

        # Canvas para el tablero
        board_frame = ctk.CTkFrame(self.root, width=400, height=400, corner_radius=10)
        board_frame.pack(pady=10)
        self.canvas = ctk.CTkCanvas(board_frame, width=400, height=400, bg="white")
        self.canvas.pack()

        # Información del juego (Movimientos y Tiempo)
        info_frame = ctk.CTkFrame(self.root)
        info_frame.pack(pady=20)
        self.moves_label = ctk.CTkLabel(
            info_frame, textvariable=self.attempts_var, font=("Arial", 14)
        )
        self.moves_label.grid(row=0, column=0, padx=10)

        self.time_label = ctk.CTkLabel(
            info_frame, textvariable=self.time_var, font=("Arial", 14)
        )
        self.time_label.grid(row=0, column=1, padx=10)

        self.update_timer()  # Inicia la actualización del tiempo

        # Barra de botones (Salir y Menú)
        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=10, fill="x")

        self.quit_button = ctk.CTkButton(
            button_frame, text="Salir", command=self.root.destroy, fg_color="#cc4437"
        )
        self.quit_button.pack(side="left", padx=20, pady=10)

        self.menu_button = ctk.CTkButton(
            button_frame, text="Volver al Menú", command=self.back_to_menu, fg_color="#348536"
        )
        self.menu_button.pack(side="right", padx=20, pady=10)

        # Inicializar el tablero
        self.draw_grid()
        self.shuffle_grid()
        self.canvas.bind("<Button-1>", self.on_click)

    
    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.time_var.set(f"Tiempo: {elapsed_time:.0f}s")  # actualiza el StringVar
            self.root.after(1000, self.update_timer)  # actualiza cada segundo

    def draw_grid(self):
        self.tiles = []
        self.canvas.delete("all")
        cell_size = 400 // self.size
        offset = (400 - (cell_size * self.size)) // 2

        for i in range(self.size):
            for j in range(self.size):
                num = self.grid[i][j]
                x1, y1 = j * cell_size + offset, i * cell_size + offset
                x2, y2 = x1 + cell_size, y1 + cell_size
                if num != 0:
                    tile = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="lightblue", outline="black")
                    text = self.canvas.create_text(
                        x1 + cell_size // 2, y1 + cell_size // 2, text=str(num), font=("Arial", 24))
                    self.tiles.append((tile, text))

    def shuffle_grid(self):
        nums = list(range(self.size * self.size))
        random.shuffle(nums)
        while not self.is_solvable(nums):
            random.shuffle(nums)
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = nums.pop(0)
        self.empty_tile = next((i, j) for i in range(self.size)
                               for j in range(self.size) if self.grid[i][j] == 0)
        self.draw_grid()

    def is_solvable(self, nums):
        inversions = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] and nums[j] and nums[i] > nums[j]:
                    inversions += 1
        return inversions % 2 == 0

    def on_click(self, event):
        x, y = event.x, event.y
        cell_size = 400 // self.size
        offset = (400 - (cell_size * self.size)) // 2

        row = (y - offset) // cell_size
        col = (x - offset) // cell_size

        if 0 <= row < self.size and 0 <= col < self.size:
            if self.move_tile(row, col):
                self.draw_grid()
                self.attempts += 1
                self.attempts_var.set(f"Movimientos: {self.attempts}")
                if self.is_solved():
                    self.win_game()

    def move_tile(self, row, col):
        empty_row, empty_col = self.empty_tile

        if (abs(empty_row - row) == 1 and empty_col == col) or (abs(empty_col - col) == 1 and empty_row == row):
            self.grid[empty_row][empty_col], self.grid[row][col] = self.grid[row][col], self.grid[empty_row][empty_col]
            self.empty_tile = (row, col)
            return True
        return False

    def is_solved(self):
        return self.grid == [[(i * self.size + j + 1) % (self.size * self.size) for j in range(self.size)] for i in range(self.size)]

    def win_game(self):
        self.canvas.create_text(200, 200, text="¡Ganaste!", font=("Arial", 36), fill="green")
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        self.save_history(elapsed_time)

    def back_to_menu(self):
        self.root.destroy()
        game_menu()
    
    def save_history(self, elapsed_time=None):
        with open("history.txt", "a") as file:
            file.write(f"{self.name} : {self.attempts} : {self.mode} : {elapsed_time:.2f}\n")
            
    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

def game_menu():
    def submit_name():
        user_name = entry.get()
        if not user_name or user_name.isspace():
            messagebox.showerror("Error", "Debe ingresar un nombre")
            return
        difficulty = difficulty_var.get()
        root.destroy()
        start_game(user_name, difficulty)

    def view_history():
        root.destroy()
        show_history()

    root = ctk.CTk()
    root.title("Menú Principal")
    SlidingPuzzle.center_window(None, root, 450, 350)  # Centra la ventana

    # Título del menú
    title_label = ctk.CTkLabel(
        root, 
        text="¡Bienvenido al Sliding Puzzle!", 
        font=("Arial", 20, "bold")
    )
    title_label.pack(pady=20)

    # Sección para ingresar el nombre
    name_frame = ctk.CTkFrame(root)
    name_frame.pack(pady=10, padx=20, fill="x")

    name_label = ctk.CTkLabel(name_frame, text="Ingrese su nombre:", font=("Arial", 14))
    name_label.pack(side="left", padx=5)

    entry = ctk.CTkEntry(name_frame, font=("Arial", 12))
    entry.pack(side="left", padx=5, fill="x", expand=True)

    # Sección para seleccionar la dificultad
    difficulty_label = ctk.CTkLabel(
        root, 
        text="Seleccione la dificultad:", 
        font=("Arial", 14)
    )
    difficulty_label.pack(pady=10)

    difficulty_var = ctk.StringVar(value="Normal")
    difficulty_options = ["Fácil", "Normal", "Medio", "Difícil"]
    difficulty_frame = ctk.CTkFrame(root)
    difficulty_frame.pack(pady=5, padx=20, fill="x")

    for option in difficulty_options:
        ctk.CTkRadioButton(
            difficulty_frame, 
            text=option, 
            variable=difficulty_var, 
            value=option,
            font=("Arial", 12)
        ).pack(side="left", padx=5, pady=5)

    # Sección de botones
    button_frame = ctk.CTkFrame(root)
    button_frame.pack(pady=20)

    history_button = ctk.CTkButton(
        button_frame, 
        text="Historial de juegos", 
        command=view_history, 
        font=("Arial", 12), 
        width=120
    )
    history_button.pack(side="left", padx=10)

    start_button = ctk.CTkButton(
        button_frame, 
        text="Iniciar", 
        command=submit_name, 
        fg_color="#348536",
        font=("Arial", 12), 
        width=120
    )
    start_button.pack(side="left", padx=10)

    # Pie de página
    footer_label = ctk.CTkLabel(
        root, 
        text="Desarrollado por FrankSkep", 
        font=("Arial", 10), 
        text_color="gray"
    )
    footer_label.pack(pady=10)

    root.mainloop()

def show_history():
    def back_to_menu():
        history_window.destroy()
        game_menu()

    history_window = ctk.CTk()
    history_window.title("Historial de Partidas")
    SlidingPuzzle.center_window(None, history_window, 500, 550)  # Centra la ventana

    label = ctk.CTkLabel(history_window, text="Historial de Partidas", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    # Marco desplazable para la tabla
    scrollable_frame = ctk.CTkScrollableFrame(history_window, width=460, height=400)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Agregar encabezados centrados
    headers = ["Jugador", "Movimientos", "Modo", "Tiempo (S)"]
    for col, header in enumerate(headers):
        header_label = ctk.CTkLabel(scrollable_frame, text=header, font=("Arial", 14, "bold"))
        header_label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
        scrollable_frame.grid_columnconfigure(col, weight=1)  # Centrar columnas

    # Leer y procesar el historial
    try:
        with open("history.txt", "r") as file:
            history_content = file.readlines()
    except FileNotFoundError:
        history_content = []

    # Mostrar datos en la tabla
    for row, line in enumerate(history_content, start=1):
        try:
            player, attempts, mode, time = line.strip().split(" : ")
        except ValueError:
            player, attempts, mode, time = "Desconocido", "N/A", "N/A", "N/A"
        data = [player, attempts, mode, time]
        for col, value in enumerate(data):
            cell_label = ctk.CTkLabel(scrollable_frame, text=value, font=("Arial", 12))
            cell_label.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")

    # Botón para volver al menú
    back_button = ctk.CTkButton(history_window, text="Volver al Menú", command=back_to_menu)
    back_button.pack(pady=10)

    history_window.mainloop()

def start_game(user_name, difficulty):
    root = ctk.CTk()
    size = {"Fácil": 3, "Normal": 4, "Medio": 5, "Difícil": 6}[difficulty]
    app = SlidingPuzzle(root, size)
    app.name = user_name
    app.mode = difficulty
    app.start_time = time.time()
    root.mainloop()


if __name__ == "__main__":
    game_menu()
