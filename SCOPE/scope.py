#Scope (alcance de variables): determina desde qué partes del programa podemos acceder a una variable.
# - Variable local: se crea dentro de una función y solo está disponible dentro de su ámbito.
# - Variable global: se crea fuera de las funciones y puede consultarse desde ellas.

#def ejemplo():
#    mensaje = "Hola Python"
#    return mensaje
#print(ejemplo())

contador = 10 #variable global

def aumentar(contador):
    resultado= contador + 1
    return resultado

resultado=aumentar(contador)
print(resultado)

def calcular_descuento(precio,descuento):
    descuento_total= precio - (precio * descuento)  #variable local.
    return descuento_total

resultado=calcular_descuento(800,0.15)
print(resultado)