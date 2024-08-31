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

if opcion_usuario == opcion_pc:
    print("* Empate *")
elif opcion_usuario == 1:
    if opcion_pc == 2:
        print("* Perdiste *")
    else:
        print("* Ganaste *")
elif opcion_usuario == 2:
    if opcion_pc == 1:
        print("* Ganaste *")
    else:
        print("* Perdiste *")
else:
    if opcion_pc == 1:
        print("* Perdiste *")
    else:
        print("* Ganaste *")
