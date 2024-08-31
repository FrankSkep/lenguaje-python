N_CALIF = 3
calif1, calif2, calif3, prom = 0, 0, 0, 0
8
calif1 = float(input("Ingresa calificacion 1: "))
calif2 = float(input("Ingresa calificacion 2: "))
calif3 = float(input("Ingresa calificacion 3: "))

prom = (calif1 + calif2 + calif3) / N_CALIF

if prom >= 80:
    if prom >= 98:
        if prom <= 100:
            print("Excelente")
        else:
            print("Error en promedio.")
    else:
        if prom < 90:
            print("Bien")
        else:
            print("Muy bien")
else:
    if prom >= 60:
        if prom < 70:
            print("Suficiente")
        else:
            print("Regular")
    else:
        if prom >= 30:
            print("Extraordinario")
        else:
            print("Repetir")