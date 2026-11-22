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
# while not numero_valido2: #mientras numero valido sea falso osea no sea validado.
    
#     try:


#         if n2==0:
#                 print("No puedes dividir entre 0.")
#         else:
#              numero_valido2 =True #cuando valida que no es un 0 y si es un numero y no un str pues sale del while.
#     except ValueError:
#         print("Diga un numero valido.")

# def dividir(n1,n2):
#     numero_valido2:False
#     while not numero_valido2:
#         try:
#             n1=float(input("Diga el primer numero: "))
#             n2=float(input("Diga el segundo numero:  "))    

#             if n2==0:
#                 print("No puedes dividir entre 0.")
#             else:
#               numero_valido2 =True #cuando valida que no es un 0 y si es un numero y no un str pues sale del while.
#         except ValueError:
#             print("Diga un numero valido.")
#     return n1/n2
# resultado = dividir(n1, n2)

# print("Resultado:", resultado)
# resta=restar(n1,n2)
# print("El resultado de la resta es:",resta)

n1=None #inicializa variables pero sin valor
n2=None
print("||||||||||| CALCULADORA ||||||||||||")
opcion=int(input("Elige una opcion\n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir\n"))




def sumar(n1,n2):
    return n1+n2
def restar(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

while opcion != 5:
    if opcion >=5 or opcion <=0:
            print("por favor seleccione una opcion valida")
            opcion=int(input("Elige una opcion\n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir\n"))
    else:
        match opcion:
            case 1: 
                nValido=False
                while not nValido:
                    try:
                        n1=float(input("Diga el primer numero: "))
                        n2=float(input("Diga el segundo numero:  "))
                        nValido=True
                    except ValueError:
                        print("Diga un numero valido")
                suma=sumar(n1,n2)
                print("N1:", n1)
                print("N2:", n2)
                print(f"La suma de {n1} + {n2} es: ", suma)
                

            case 2:
                nValido=False
                while not nValido:
                    try:
                        n1=float(input("Diga el primer numero: "))
                        n2=float(input("Diga el segundo numero:  "))
                        nValido=True
                    except ValueError:
                        print("Diga un numero valido")
                resta=restar(n1,n2)
                print("N1:", n1)
                print("N2:", n2)
                print("El resultado de la resta es: ",resta)
                
            case 3:
                nValido=False
                while not nValido:
                    try:
                        n1=float(input("Diga el primer numero: "))
                        n2=float(input("Diga el segundo numero:  "))
                        nValido=True
                    except ValueError:
                        print("Diga un numero valido")
                multiplicacion=multiplicar(n1,n2)
                print("El resultado de la multiplicacion es: ",multiplicacion)
                
            case 4:
                nValido=False
                numero_valido2=False
                while not nValido or not numero_valido2:
                    try:
                        n1=float(input("Diga el primer numero: "))
                        n2=float(input("Diga el segundo numero:  "))
                        nValido=True
                        
                        if n2 == 0:
                            print("No puedes dividir entre 0")
                            numero_valido2=False
                        else:
                            numero_valido2=True
                    except ValueError:
                        nValido=False # Se cambia a False por que en caso de que el usuario haya puesto un 0  antes pues ya se habra cambiado a true entonces por eso lo volvemos a poner en false.
                        print("Diga un numero valido")
                        
                resultado_division=division(n1,n2)
                print("El resultado de la division es: ",resultado_division)