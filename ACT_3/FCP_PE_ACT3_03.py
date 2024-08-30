from franLib import getNumber
# constantes
LOCAL = 3.0
NACIONAL = 7.0
INTL = 9.0
IVA = 0.16

# entrada
minutos = getNumber("Ingrese minutos de la llamada: ")
tipo_llamada = getNumber("Ingrese tipo de Llamada\n1. Local\n2. Nacional\n3. Internacional\n: ")

# variables necesarias
subtotal, min_adicionales, total = 0, 0, 0

# calculos
if tipo_llamada == 1:
    subtotal = LOCAL
elif tipo_llamada == 2:
    subtotal = NACIONAL
    if minutos > 3:
        min_adicionales = minutos - 3
        subtotal += min_adicionales * 2
elif tipo_llamada == 3:
    subtotal = INTL
    if minutos > 2:
        min_adicionales = minutos - 2
        subtotal += min_adicionales * 4
else:
    print("Opcion no valida.")

# resultado
total = subtotal + (subtotal * IVA)
print(f"> Subtotal: {subtotal}\n> IVA: {subtotal * IVA}\n> Total: {total}")