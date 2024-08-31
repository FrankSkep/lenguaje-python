# Precios de los productos
precios = {
    'computadora': 1000,
    'impresora': 200,
    'television': 800,
    'barra_sonido': 150,
    'consola': 500,
    'juego': 60
}

# Lista de productos en el carrito
carrito = []

while (True):
    print("¿Que producto desea agregar al carrito?")
    print("1.- Computadora")
    print("2.- Impresora")
    print("3.- Television")
    print("4.- Barra de sonido")
    print("5.- Consola")
    print("6.- Juego")
    print("0.- Es todo")
    op = int(input("Opcion: "))

    if op == 1:
      if 'computadora' not in carrito:
        carrito.append('computadora')
    elif op == 2:
      if 'impresora' not in carrito:
        carrito.append('impresora')
    elif op == 3:
      if 'television' not in carrito:
        carrito.append('television')
    elif op == 4:
      if 'barra_sonido' not in carrito:
        carrito.append('barra_sonido')
    elif op == 5:
      if 'consola' not in carrito:
        carrito.append('consola')
    elif op == 6:
      if 'juego' not in carrito:
        carrito.append('juego')
    if op == 0:
        break
    print("Carrito: ", carrito)

# Total a pagar
total = 0

if 'computadora' in carrito:
    total += precios['computadora'] * 0.95
    if 'impresora' in carrito:
        total += precios['impresora'] * 0.90
else:
    if 'impresora' in carrito:
        total += precios['impresora']

if 'television' in carrito:
    total += precios['television'] * 0.93
    if 'barra_sonido' in carrito:
        total += precios['barra_sonido'] * 0.85
else:
    if 'barra_sonido' in carrito:
        total += precios['barra_sonido']

if 'consola' in carrito:
    total += precios['consola'] * 0.90
    if 'juego' in carrito:
        total += precios['juego'] * 0.80
else:
    if 'juego' in carrito:
        total += precios['juego']

print(f"El precio total a pagar es: ${total:.2f}")
