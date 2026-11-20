
#Requisitos
#El programa debe permitir:
#1. Registrar estudiantes.
#2. Guardar tres calificaciones por estudiante.
#3. Calcular el promedio de cada estudiante.
#4. Mostrar todos los estudiantes registrados.
#5. Indicar si cada estudiante aprobó o reprobó. La calificación mínima para aprobar será 6

# .Restricciones
#- Utiliza listas y diccionarios.
#- Organiza el programa mediante funciones.
#- No repitas código innecesariamente.
#- Valida que las calificaciones estén entre 0 y 10.
#- No utilices clases todavía; más adelante lo convertiremos a POO.
#HELLO WORLD
estudiantes = [] # es importante crear una lista para que no se confunda el programa y guarde las calificaciones de una persona diferente en la misma lista.


print("\n===== SISTEMA DE CALIFICACIONES =====\n ")
print("1. Registrar estudiante\n2. Mostrar estudiantes\n3. Buscar estudiante\n4. Calcular promedios\n5. Salir")
opcion= int(input("Seleccione una opcion: "))
def registrar_estudiantes(): #para hacer una funcion se usa def primero seguido del nombre de la funciion doble parentesis y dos puntos ejemplo def nombre_funcion():  
    duplicado=False #para verificar que un numero es duplicado o no
    nombre=input("Di el nombre del estudiante: ").lower().strip() 
    for estudiante in estudiantes:
        if nombre == estudiante["nombre"].lower().strip():
            print("El nombre ya fue registrado.")
            duplicado=True
    if duplicado == True:
        print("No puede continuar con el registro")
    else:
        edad=int(input("Di la edad del estudiante: "))
        while edad <=0:
            print("Edad Invalida")
            edad=int(input("Di la edad del estudiante: "))
        calificaciones=[]
        for i in range(3): 
            nota=float(input("Di la calificacion del estudiante: "))
            while nota < 0 or nota > 10: 
                print("Calificacion Invalida")  
                nota=float(input("Vuelve a dar otra calificacion que si sea valida."))
            calificaciones.append(nota)
        estudiante = { #ESTO ES UN DICCIONARIO SE USA PARA ALMACENAR INFORMACION DE ALGO O ALGUIEN EN UN ARREGLO, FALTA USAR APPEND.
            "nombre": nombre,
            "edad": edad,
            "calificaciones":calificaciones
        }
        print("Se ha confirmado el registro de estudiante exitosamente.")
        estudiantes.append(estudiante) #lista.append(elemento) 
def mostrar_estudiantes():
    if not estudiantes: #not sirve literalmente como un no, ahi diria, si no hay estudiantes xd
        print("No hay estudiantes actualmente.")
    else:
        for estudiante in estudiantes: #for que muestra la informacion de los estudiantes.
            
            print(estudiante["nombre"]) #sirve para entrar al diccionario y agarrar la informacion
            print(estudiante["edad"])
            print(estudiante["calificaciones"])
            print("------------------------")

def promedio_estudiantes():
    if not estudiantes:
        print("No hay estudiantes para promediar")
    else:
        for estudiante in estudiantes:
            calificaciones = estudiante["calificaciones"]
            nombre_estudiante=estudiante["nombre"] #sirve para traer el nombre de las personas del diccionario
            suma= sum(calificaciones)
            cantidad_calificaciones=len(calificaciones)
            promediofinal= suma/cantidad_calificaciones
            print(f"El promedio final de {nombre_estudiante} es de {promediofinal:.2f}\n") #el :.2f lo que hace es mostrar solo 2 decimales.
            if promediofinal >= 6   :
                print("Felicidades. Haz aprobado")
                
            else:
                print("Lo lamento. Haz reprobado")
def buscar_estudiante():
    busqueda=input("dime el estudiante a buscar ").lower().strip() #.lower convierte todas las letras de una cadena de texto a minusculas.
    for estudiante in estudiantes:
        nombre_estudiante=estudiante["nombre"].lower().strip() #.strip elimina espacios innecesarios.
        if busqueda == nombre_estudiante:
            print("encontraste al usuario")
            print(estudiante["nombre"]) 
            print(estudiante["edad"])
            print(estudiante["calificaciones"])
            break
    else:
        print("No encontraste el usuario")

             
        
        

while opcion !=5:
    print("\n===== SISTEMA DE CALIFICACIONES =====\n ")
    print("1. Registrar estudiante\n2. Mostrar estudiantes\n3. Buscar estudiante\n4. Calcular promedios\n5. Salir")
    opcion= int(input("Seleccione una opcion: "))
    
    if opcion >=6 or opcion <=0:
        print("por favor seleccione una opcion valida")
        
        
    else:
        match opcion:
            case 1:
                registrar_estudiantes()     
                
                    
                    

            case 2: 
                mostrar_estudiantes()
            case 3:
                buscar_estudiante()

            case 4: 
                promedio_estudiantes()
            case _:
                print("Opcion no valida")
                print("por favor seleccione una opcion valida")
    
        



