
# try: # Es un bloque donde colocamos instrucciones que podrian generar erroores. INTENTA EJECUTAR EL CODIGO.
#     edad=int(input("Ingresa tu edad: "))
    
#     if edad <= 0:
#         print("Ingresa una edad valida")
#     else:
#         print(edad)
# except ValueError: #CAPTURA ERRORES SI EL USUARIO NO PONE UN
#     print("Debes ingreasr un numero valido. ")        
    

edad_valida = False
while edad_valida == False:
    try: #dice algo que puede tener errores.
        edad = int(input("Ingresa tu edad: "))
        
        if edad <= 0: 
            print("Ingrese una edad valida")
            
        else: #cuando edad_valida=true se cierra el while.
            edad_valida=True
            print(f"Tienes {edad} años")
    except ValueError:
        print("Ingresa un numero valido.")

