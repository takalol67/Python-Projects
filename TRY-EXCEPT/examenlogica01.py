# Recorra todos los números.
# Identifique cuáles son mayores o iguales a 7.
# Cuente cuántos cumplen la condición.
# Calcule la suma de esos números.
numeros = [4, 9, 2, 7, 12, 5, 8]
contador= 0 #Un contador sirve para contar cuántas veces sucede algo.
suma=0 #acumulador Un acumulador sirve para guardar una cantidad que va aumentando o cambiando conforme procesamos datos.
for numero in numeros:
    if numero >= 7:
        contador+=1
        
        suma+=numero
print(contador)
print(suma)

