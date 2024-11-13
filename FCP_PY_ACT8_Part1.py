import customtkinter as ctk

ctk.set_appearance_mode("light")  # tema
ctk.set_default_color_theme("blue")  # color de tema

app = ctk.CTk()
app.title("Calculadora Operaciones Básicas")
app.geometry("480x300")


numero1_var = ctk.StringVar(value="0")
numero2_var = ctk.StringVar(value="0")
resultado_var = ctk.StringVar(value="0")

# Funciones para las operaciones
def sumar():
    resultado_var.set(str(float(numero1_var.get()) + float(numero2_var.get())))

def restar():
    resultado_var.set(str(float(numero1_var.get()) - float(numero2_var.get())))

def multiplicar():
    resultado_var.set(str(float(numero1_var.get()) * float(numero2_var.get())))

def dividir():
    try:
        resultado_var.set(str(float(numero1_var.get()) / float(numero2_var.get())))
    except ZeroDivisionError:
        resultado_var.set("Error")

# Marco para las operaciones
frame_operaciones = ctk.CTkFrame(app)
frame_operaciones.pack(pady=10, padx=10, fill="x")

# Labels y Entrys
ctk.CTkLabel(frame_operaciones, text="Num. 1", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=5)
entry_numero1 = ctk.CTkEntry(frame_operaciones, textvariable=numero1_var, width=60, font=("Arial", 18))
entry_numero1.grid(row=0, column=1)

ctk.CTkLabel(frame_operaciones, text="Num. 2", font=("Arial", 18)).grid(row=0, column=2, padx=10, pady=5)
entry_numero2 = ctk.CTkEntry(frame_operaciones, textvariable=numero2_var, width=60, font=("Arial", 18))
entry_numero2.grid(row=0, column=3)

ctk.CTkLabel(frame_operaciones, text="Resultado", font=("Arial", 18)).grid(row=0, column=4, padx=10, pady=5)
entry_resultado = ctk.CTkEntry(frame_operaciones, textvariable=resultado_var, width=60, state="readonly", font=("Arial", 18))
entry_resultado.grid(row=0, column=5)

# Marco para los operadores
frame_operadores = ctk.CTkFrame(app)
frame_operadores.pack(pady=10, padx=10)

# Botones
btn_suma = ctk.CTkButton(frame_operadores, text="+", command=sumar, width=70, height=40, font=("Arial", 18))
btn_suma.grid(row=0, column=0, padx=5, pady=5)

btn_resta = ctk.CTkButton(frame_operadores, text="-", command=restar, width=70, height=40, font=("Arial", 18))
btn_resta.grid(row=0, column=1, padx=5, pady=5)

btn_multiplicacion = ctk.CTkButton(frame_operadores, text="×", command=multiplicar, width=70, height=40, font=("Arial", 18))
btn_multiplicacion.grid(row=0, column=2, padx=5, pady=5)

btn_division = ctk.CTkButton(frame_operadores, text="÷", command=dividir, width=70, height=40, font=("Arial", 18))
btn_division.grid(row=0, column=3, padx=5, pady=5)

if __name__ == "__main__":
    app.mainloop()

if __name__ == "__main__":
    app.mainloop()
