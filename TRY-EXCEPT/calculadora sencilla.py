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
n1=None #inicializa variables pero sin valor
n2=None
numero_valido2=False
print("||||||||||| CALCULADORA ||||||||||||")
opcion=int(input(("Elige una opcion\n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir")))
while not numero_valido2: #mientras numero valido sea falso osea no sea validado.
    
    try:
        n1=float(input("Diga el primer numero: "))
        n2=float(input("Diga el segundo numero:  "))
        
        if n2==0:
                print("No puedes dividir entre 0.")
        else:
             numero_valido2 =True #cuando valida que no es un 0 y si es un numero y no un str pues sale del while.
    except ValueError:
        print("Diga un numero valido.")
  
def dividir(n1,n2):
 
    return n1/n2

def sumar(n1,n2):
    return n1+n2
def restar(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2
print("N1:", n1)
print("N2:", n2)

resultado = dividir(n1, n2)

print("Resultado:", resultado)

suma=sumar(n1,n2)
print("El resultado de la suma es:",suma)


resta=restar(n1,n2)
print("El resultado de la resta es:",resta)

while opcion <=5:
    match opcion:
        case 1: 
    


