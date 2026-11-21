# Vamos a crear una calculadora que:
# - Pida dos números.
# - Permita sumar, restar, multiplicar y dividir.
# - Controle entradas inválidas (ValueError).
# - Evite divisiones entre cero (ZeroDivisionError).
# Primer paso: crea una función llamada dividir(numero1, numero2) que:
# 1. Reciba dos números.
# 2. Compruebe si numero2 es igual a cero.
# 3. Si es cero, muestre un mensaje.
# 4. Si no es cero, devuelva el resultado mediante return.

def dividir(n1,n2):
    numero1=float(input("Diga el primer numero a dividir."))
    numero2=float(input("Diga el segundo numero a dividir"))
    n1=numero1
    n2=numero2
    division= numero1/numero2
    return division
    