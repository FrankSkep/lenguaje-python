from franLib import getNumber

# constantes
RANGO_1 = 4
RANGO_2 = 15
RANGO_3 = 50
IVA = 0.16

m3 = getNumber("Ingrese los M3 de agua consumidos: ")

# Calcular el subtotal según el rango de consumo
if m3 <= RANGO_1:
    subtotal = 50
elif m3 <= RANGO_2:
    subtotal = 50 + (m3 - RANGO_1) * 8
elif m3 <= RANGO_3:
    subtotal = 50 + (11 * 8) + (m3 - RANGO_2) * 10
else:
    subtotal = 50 + (11 * 8) + (35 * 10) + (m3 - RANGO_3) * 11

print(f"Subtotal: {subtotal}")
print(f"Iva: {subtotal * IVA}")
print(f"Total a pagar: {subtotal + (subtotal * IVA)}")
