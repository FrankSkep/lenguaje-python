import os

# Limpia pantalla para cualquier sistema
def clear() -> None:
    if os.name == 'nt':  # Si es Windows
        os.system('cls')
    else:  # Si es Unix
        os.system('clear')

# Pausa el programa hasta que se presione enter
def pause() -> None:
    input("Presiona enter para continuar")

# Verifica que se ingrese un valor numerico, si no se proporciona tipo, sera int
def getNumber(msg: str, tipo: type = int) -> type:
    while True:
        numero = input(msg)
        try:
            return tipo(numero)
        except ValueError:
            print(f"Error: Ingresa un numero {tipo.__name__} valido.")

# Verifica que se ingrese un valor numerico de cualquier tipo en un rango
def getNumber_R(msg: str, ri, rf, tipo: type = int) -> type:
    while True:
        num_str = input(msg)
        try:
            num = tipo(num_str)
            if num >= ri and num <= rf:
                return num
            else:
                print("Error: Ingresa un numero dentro del rango.")
        except ValueError:
            print(f"Error: Ingresa un numero {tipo.__name__} valido.")
