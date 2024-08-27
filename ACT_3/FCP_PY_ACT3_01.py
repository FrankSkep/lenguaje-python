def getNum(msg: str, tipo: type = int):
    valido = False
    while not valido:
        try:
            num = input(msg)
            return tipo(num)
        except:
            print("Ingresa solo numeros.")
            valido = False


N_CALIF = 3
calif1, calif2, calif3, prom = 0, 0, 0, 0

calif1 = getNum("Ingresa calificacion 1: ", float)
calif2 = getNum("Ingresa calificacion 2: ", float)
calif3 = getNum("Ingresa calificacion 3: ", float)

prom = (calif1 + calif2 + calif3) / N_CALIF

if prom < 100:
    if prom >= 98:
        print("Excelente")
    elif prom >= 90:
        print("Muy bien")
    elif prom >= 80:
        print("Bien")
    elif prom >= 70:
        print("Regular")
    elif prom >= 60:
        print("Suficiente")
    elif prom >= 30:
        print("Extraordinario")
    else:
        print("Repetir")
else:
    print("Error en promedio")
