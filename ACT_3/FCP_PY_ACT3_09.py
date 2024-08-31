precio = float(input("> Ingrese precio del producto: "))
temporada = input("> Ingresa temporada (verano, invierno, primavera, otoño): ").lower()
etiqueta = input("> Ingrese la etiqueta del producto (roja, verde, amarilla) o enter si no tiene etiqueta: ").lower()
descuento = 0

if temporada == "verano":
  descuento = 0.20
elif temporada == "invierno":
  if etiqueta == "rojo":
    descuento = 0.30
  elif etiqueta == "verde":
    descuento = 0.15
elif temporada in ["primavera", "otoño"]:
  if etiqueta == "amarillo":
    descuento = 0.10

precio_final = precio * (1 - descuento)
print(f"El precio a pagar es: {precio_final:.2f}")