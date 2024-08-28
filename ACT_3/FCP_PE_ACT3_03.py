"""
3.- Algoritmo que sirva para desplegar el Total de una llamada telefónica donde se pide como datos de
entrada los minutos y el tipo de llamada, se cobra de la siguiente manera:
1.- Llamada Local $3.00 sin límite de tiempo
2.- Llamada Nacional $7.00 por los 3 primeros minutos y $2.00 minuto adicional
3.- Llamada Internacional $9.00 por los 2 primeros minutos y $4.00 minuto adicional
Desplegar, Subtotal,Iva (16%) y Total.
"""
# constantes
LOCAL = 3.0
NACIONAL = 7.0
INTL = 9.0
IVA = 0.16

# entrada
minutos = int(input("Ingrese minutos de la llamada: "))
tipo_llamada = int(input("Tipo Llamada\n1. Local\n2. Nacional\n3. Internacional"))

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