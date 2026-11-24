movimientos=[]

def registraringresos(movimientos):
    descripcion= input("Describa su ingreso: ")
    valor_valido=False
    while not valor_valido:
        try:
            cantidad=float(input("Diga la cantidad que desea ingresar: "))
            if cantidad <=0:
                print("Agregue un numero valido")
            else:
                valor_valido=True
        except ValueError:
            valor_valido=False
            print("Diga una cantidad valida.")
    tipo="ingreso"
    categoria=input("Diga la categoria: ")
    movimiento = {
        "descripcion": descripcion,
        "cantidad": cantidad,
        "categoria": categoria,
        "tipo": tipo
    }
    movimientos.append(movimiento)
    return movimiento

resultado=registraringresos(movimientos)
print(resultado)
print(movimientos)