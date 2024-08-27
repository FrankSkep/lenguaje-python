minutos, tipo_llamada = None, None

LOCAL = 3.0
NACIONAL = 7.0
INTL = 9.0
IVA = 0.16

minutos = int(input("Ingrese minutos de la llamada: "))
tipo_llamada = int(input("Tipo Llamada\n1. Local\n2. Nacional\n3. Internacional"))

costo = 0
minutos_adicionales = 0

if minutos <= 3:
    if tipo_
else:
    

if tipo_llamada == 1:
    costo = LOCAL
elif tipo == 2:
    if minutos > 3:
        minutos_adicionales = minutos - 3
        
    if minutos <= 3:
        costo = NACIONAL
        costo += 
    
elif tipo == 3:

else:
    print("Opcion no valida.")