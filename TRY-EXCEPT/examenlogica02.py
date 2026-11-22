# Contar números pares.
# Contar números impares.
# Sumar números pares.res.
# calcular el promedio de los impares.
numeros = [12, 5, 18, 3, 20, 7, 15, 2]
contadorpar = 0
contadorimpar = 0
sumapares=0
sumaimpares=0
for numero in numeros:
    if numero % 2 == 0:
        print("El numero es par.")
        contadorpar+=1
        sumapares+=numero
    elif numero %2 == 1:
        print("el numero es impar.")
        contadorimpar+=1
        sumaimpares+=numero
        
print(contadorpar)
print(contadorimpar)
print(sumapares)
print(sumaimpares/contadorimpar)