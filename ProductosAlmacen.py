def procesar_productos(productos):
    pedidos_urgentes = []
    valor_total = 0

    for producto in productos:
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        precio = producto["precio"]

        # 1. Identificar productos con poco stock
        if cantidad < 5:
            pedidos_urgentes.append(nombre)

        # 2. Calcular valor total del inventario
        valor_total += cantidad * precio

        # 3. Aplicar clasificación Premium
        if precio > 100:
            producto["categoria"] = "Premium"
        else:
            producto["categoria"] = "Normal"

    return pedidos_urgentes, valor_total, productos


# Ejemplo
productos = [
    {"nombre": "Laptop", "cantidad": 3, "precio": 500},
    {"nombre": "Mouse", "cantidad": 10, "precio": 25},
    {"nombre": "Monitor", "cantidad": 2, "precio": 150}
]

urgentes, total, inventario = procesar_productos(productos)

print("Pedidos urgentes:", urgentes)
print("Valor total:", total)
print("Inventario:", inventario)