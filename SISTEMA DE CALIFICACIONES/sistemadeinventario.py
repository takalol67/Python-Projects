#if-else: ejecuta una alternativa cuando una condición es falsa.

#for-else: ejecuta el else cuando el ciclo termina sin un break.

print("\n===== SISTEMA DE INVENTARIO =====\n ")
print("1. Registrar productos\n2. Mostrar productos\n3.  Buscar producto por nombre.\n4. Calcular el valor total del inventario\n5.Salir")
opcion=int(input("Seleccione una opcion. "))
productos=[]
def registrar_productos():
    
    duplicado=False
    nombre=input("Di el nombre del producto. ").lower().strip()
    for producto in productos:
        if nombre == producto["nombre"]:
            print("El producto ya fue registrado")
            duplicado=True
    if duplicado == True:
            print("No puede continuar con el registro.")
    else:
            precio=float(input("Di el precio del producto. "))
            while precio < 0:
                print("No se puede poner un numero negativo.")
                precio=float(input("Di el precio del producto. "))
            
            cantidad=int(input("Di la cantidad de inventario "))
            while cantidad < 0:
                print("No se puede poner cantidades negativas.")
                cantidad=int(input("Di la cantidad del producto. "))

            
    
    

            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(producto)

def mostrar_productos():
    for producto in productos:
        print(producto["nombre"])
        print(producto["precio"])
        print(producto["cantidad"])
def buscar_productos():
    busqueda=input("Dime el producto a buscar. ").lower().strip()
    for producto in productos:
        nombre_producto=producto["nombre"].lower().strip()
        if busqueda == nombre_producto.lower().strip():
            print("Encontraste el producto.")
            print(producto["nombre"])
            print(producto["precio"])
            print(producto["cantidad"])
            break
    else:#Se utiliza el else en el for y no en el if porque necesitamos que Python termine de recorrer toda la lista para comprobar que el producto no existe. Si encuentra una coincidencia, ejecuta break y evita que se ejecute el else del for.
             print("No hay el usuario que busca. ")

def valor_total():
     total = 0
     for producto in productos:
          valor_total=producto["precio"] * producto["cantidad"]
          print(f"El precio total es de {valor_total}")
            
          total+=valor_total
     print(f"El valor total es de ${total}")
            

    
while opcion !=5:
    print("\n===== SISTEMA DE INVENTARIO =====\n ")
    print("1. Registrar productos\n2. Mostrar productos\n3.  Buscar producto por nombre.\n4. Calcular el valor total del inventario\n5.Salir")
    opcion=int(input("Seleccione una opcion. "))
    if opcion >=6 or opcion <=0:
            print("por favor seleccione una opcion valida")
    else:
        match opcion:
            case 1:
                registrar_productos()
            case 2:
                  mostrar_productos()
            case 3:
                  buscar_productos()
            case 4:
                  valor_total()