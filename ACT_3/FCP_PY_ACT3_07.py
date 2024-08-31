import random

# Opciones
opciones = {
    1: "PIEDRA",
    2: "PAPEL",
    3: "TIJERA"
}

opcion_usuario = None
opcion_pc = None

print("-+ CHINCHAMPU +-")
print("OPCIONES : 1) PIEDRA, 2) PAPEL, 3) TIJERA")

# Obtener opcion del usuario
opcion_usuario = int(input("> Ingresa tu opcion: "))
if opcion_usuario not in opciones:
    print("Opcion no valida")
    exit(1)

# Obtener opcion del PC
opcion_pc = random.randint(1, 3)

# Determinacion del resultado
print(f"(Tu): {opciones[opcion_usuario]} vs (PC): {opciones[opcion_pc]}")

match opcion_usuario:
    case 1:
        if opcion_pc == 1:
            print("* Empate *")
        elif opcion_pc == 2:
            print("* Perdiste *")
        else:
            print("* Ganaste *")
    case 2:
        if opcion_pc == 2:
            print("* Empate *")
        elif opcion_pc == 1:
            print("* Ganaste *")
        else:
            print("* Perdiste *")
    case _:
        if opcion_pc == 3:
            print("* Empate *")
        elif opcion_pc == 1:
            print("* Perdiste *")
        else:
            print("* Ganaste *")
