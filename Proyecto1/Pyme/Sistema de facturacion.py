# Definición de productos y precios
productos = {
    "pizza chicago": 2000,
    "calzoni": 3000,
    "pizza argentina": 2500,
    "pizza congreso": 2500,
    "pizza lomo": 5000,
    "pizza ricky fort": 2000,
    "pizza italiana": 2100,
    "green pizza": 1500,
    "la 12": 2500,
    "la posta": 3500,
}

bebidas = {
    "coca cola 1.5L": 900,
    "pepsi": 800,
    "fanta": 700,
    "sprite": 850,
    "fernet": 1100,
    "cerveza": 1500,
}

postres = {
    "tiramisu": 1000,
    "helado bocha": 300,
    "flan": 500,
    "ensalada de frutas": 350,
    "churros x6": 800,
    "lemon pie": 1500,
}

# Inicialización de variables
pedido = {}
total = 0

# Función para agregar productos al pedido
def agregar_al_pedido(categoria, item, cantidad):
    global total
    precio = categoria[item]
    subtotal = precio * cantidad
    pedido[item] = {"cantidad": cantidad, "subtotal": subtotal}
    total += subtotal

# Solicitar al usuario que ingrese sus pedidos
while True:
    print("\n--- Menú ---")
    print("1. Pizzas")
    print("2. Bebidas")
    print("3. Postres")
    print("4. Terminar pedido")

    categoria_elegida = input("Elige una categoría (1-4): ")

    if categoria_elegida == "4":
        break

    if categoria_elegida not in ["1", "2", "3"]:
        print("Opción no válida. Por favor, elige una opción válida.")
        continue

    if categoria_elegida == "1":
        categoria = productos
    elif categoria_elegida == "2":
        categoria = bebidas
    elif categoria_elegida == "3":
        categoria = postres

    print("\n--- Productos disponibles ---")
    for item, precio in categoria.items():
        print(f"{item} - ${precio}")

    producto_elegido = input("Elige un producto: ")

    if producto_elegido not in categoria:
        print("Producto no válido. Por favor, elige un producto válido.")
        continue

    cantidad_elegida = int(input("Indica la cantidad: "))

    agregar_al_pedido(categoria, producto_elegido, cantidad_elegida)

# Imprimir el detalle del pedido y el total
print("\nDetalle del pedido:")
for item, info in pedido.items():
    print(f'x{info["cantidad"]} "{item}"  . . . . . . . . . . . . . . . . {info["subtotal"]}')

print("\nTotal:", total)