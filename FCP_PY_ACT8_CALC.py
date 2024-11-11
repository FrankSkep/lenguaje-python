import customtkinter as ctk

class CalculadoraApp(ctk.CTk): # heredo de la clase CTk
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("400x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)

        self.display = ctk.CTkEntry(self, placeholder_text="0", justify='right', font=("Arial", 28), state='readonly')
        self.display.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

        self.create_buttons()
        
    def create_buttons(self):
        buttons_frame = ctk.CTkFrame(self)
        buttons_frame.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 1, 4)
        ]

        for button in buttons:
            if len(button) == 3:
                text, row, col = button
                rowspan, colspan = 1, 1
            else:
                text, row, col, rowspan, colspan = button

            btn = ctk.CTkButton(buttons_frame, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5, pady=5, sticky="nsew")

        for i in range(6):  # Ajuste para 6 filas
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  # Ajuste para 4 columnas
            buttons_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display.configure(state='normal')
            self.display.delete(0, 'end')
            self.display.configure(state='readonly')
        elif char == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.show_result("Hola Mundo")
            except Exception as e:
                self.show_result("Error")
        else:
            self.display.configure(state='normal')
            self.display.insert('end', char)
            self.display.configure(state='readonly')
    
    def show_result(self, content : str):
        self.display.configure(state='normal')
        self.display.delete(0, 'end')
        self.display.insert('end', content)
        self.display.configure(state='readonly')

if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()