productos = []

nombre=input("Por favor diga el nombre del producto ")
precio=float(input("Por favor diga el precio del producto "))
cantdis=int(input("Por favor diga la cantidad disponible. "))

producto = {
    "nombre": nombre,
    "precio": precio,
    "cantdis": cantdis

}
productos.append(producto) #productos.append(producto)
print(producto["nombre"])
print(producto["precio"])
print(producto["cantdis"])
valor_total=precio * cantdis
print(f"El valor total del inventario es de {valor_total} pesos")