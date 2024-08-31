dia = input("> Ingrese dia de la semana: ").lower()
menu = input("> Elija su menu (del dia, infantil, vegetariano, chef): ").lower()
precio = float(input("> Ingrese precio: "))

descuento = 0

if dia == "lunes":
  if menu == "del ddia":
    descuento = 0.10
elif dia == "martes":
  if menu == "infantil":
    descuento = 0.20
elif dia == "miercoles":
  if menu == "vegetariano":
    descuento = 0.15
elif dia == "jueves":
  if menu == "chef":
    descuento == 0.05
else:
  print("Entrada no valida.")
  exit(1)

precio_a_pagar = precio * (1 - descuento)
print(f"Precio total a pagar: {precio_a_pagar:.2f}")