import os

os.system("clear")

# Constantes
JORNADA_NORMAL = 40
H_DOBLE_RANGO = 9

# Variables necesarias
horas_trabajadas, horas_extra = None, None
salario_hora, salario_extra, salario_normal, salario_total = None, None, None, None

# Entrada
horas_trabajadas = int(input("Ingresa horas trabajadas (SEMANA): "))
salario_hora = float(input("Ingresa salario (HORA): "))

salario_normal = JORNADA_NORMAL * salario_hora

if horas_trabajadas <= JORNADA_NORMAL:
    salario_total = salario_normal
else:
    horas_extra = horas_trabajadas - JORNADA_NORMAL
    salario_extra = horas_extra * (salario_hora * 2)

    if horas_extra > H_DOBLE_RANGO:
        salario_extra = H_DOBLE_RANGO * (salario_hora * 2)
        salario_extra += (horas_extra - H_DOBLE_RANGO) * (salario_hora * 3)

    salario_total = salario_normal + salario_extra
print("+-- Resultados --+")
print(f"-> Salario por hora: {salario_hora}")
print(f"-> Horas trabajadas: {horas_trabajadas}")
print(f"-> Salario normal: ", salario_normal)
print(f"-> Salario extra: {salario_extra}")
print(f"-> Salario total: {salario_total}")
