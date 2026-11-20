def celsius_a_fahrenheit(celsius): #parametro variables que se declaran en la definición de una función y reciben valores.
    fahrenheit= celsius * 1.8 + 32
    
    return fahrenheit

resultado= celsius_a_fahrenheit(0) #argumento  valores que se proporcionan al llamar a esa función
print(resultado)


def presentar(nombre, edad):
    print(f"Soy {nombre} y tengo {edad} años")

presentar("Edgar", 18) #Argumento posicional: se asigna según su posición. 
presentar(edad=18, nombre="Edgar") #Argumento con nombre: se asigna indicando el nombre del parámetro.

#python primero realiza multilpicacion y division lueg suma y resta.
