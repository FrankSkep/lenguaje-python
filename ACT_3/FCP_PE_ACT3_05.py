ex1, ex2, ex3, ex4, ex5, prom = 0, 0, 0, 0, 0, 0

ex1 = float(input("Ingresa calificacion 1: "))
ex2 = float(input("Ingresa calificacion 2: "))
ex3 = float(input("Ingresa calificacion 3: "))
ex4 = float(input("Ingresa calificacion 4: "))
ex5 = float(input("Ingresa calificacion 5: "))

cal_menor = ex1

# Evaluaciones
if ex2 < cal_menor:
    cal_menor = ex2
elif ex3 < cal_menor:
    cal_menor = ex3
elif ex4 < cal_menor:
    cal_menor = ex4
elif ex5 < cal_menor:
    cal_menor = ex5

prom = (ex1 + ex2 + ex3 + ex4 + ex5 - cal_menor) / 4

print(f"Calificacion anulada: {cal_menor}")

print(f"Promedio final: {prom}")
