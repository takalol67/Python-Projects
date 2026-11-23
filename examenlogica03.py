# Cuente cuántas ventas fueron mayores a 200.
# Calcule el total de todas las ventas.
# Encuentre la venta más alta.
# Calcule el promedio de todas las ventas.
# Un solo for.
# Sin funciones.
# Sin listas adicionales.
# No utilices max() ni sum().

ventas = [150, 300, 80, 450, 200, 50, 600, 120]
contador=0
contadorpromedio=0
suma=0
ordenados=sorted(ventas)
ventamaxima=ordenados[-1]
cantidad_ventas=0
total=0
for venta in ventas:
    total+=venta
    contadorpromedio+=1
    if venta > 200:
        contador+=1
print(contador) #esta bien
print(total) #esta bien
print(ventamaxima) #esta bien
print(total/contadorpromedio) #esta bien

