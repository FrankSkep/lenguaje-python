descuentos= {
    "lunes": {"del dia": 0.10},
    "martes": {"infantil": 0.20},
    "miercoles": {"vegetariano": 0.15},
    "jueves": {"chef": 0.05},
    "viernes": {"dia", 0.05},
    "sabado": {},
    "domingo": {}
}

descuento = 0
dia = input("> Ingrese dia de la semana: ").lower()
menu = input("> Elija el menu (del dia, infantil, vegetariano, chef): ").lower()
precio = float(input("> Ingrese precio: "))

if dia in descuentos:
  if menu in descuentos[dia]:
    descuento = descuentos[dia][menu]
else:
  print("Entrada no valida.")
  exit(1)

total = precio * (1 - descuento)
print(f"Precio total a pagar: {total:.2f}")