# Vamos a crear una calculadora que:
# - Pida dos números.
# - Permita sumar, restar, multiplicar y dividir.
# - Controle entradas inválidas (ValueError).
# - Evite divisiones entre cero (ZeroDivisionError).
# def dividir(n1,n2):
#     numero_valido= False
#     while not numero_valido:
#         try:
#             if n2 ==0:
#                 print("Por favor diga un numero valido q no sea 0   ")
                
#             else:
#                 numero_valido=True
#                 division=n1/n2
#                 return division
#         except ValueError:
#             print("Di un numero valido.")
# None representa la ausencia de un valor en python
def dividir(n1,n2):
 return n1/n2
            division= n1/n2
            cero=True
            return division
            

    
        

numero_valido2=False
cero=False
while not numero_valido2 and cero:
    try:
        n1=float(input("Diga el primer numero: "))
        n2=float(input("Diga el segundo numero:  "))
        numero_valido2=True
    except ValueError:
        print("Diga un numero valido.")
    except ZeroDivisionError:
        print("No puedes dividir entre 0.")
        n2=float(input("Diga el segundo numero:  "))
