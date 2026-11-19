#number guessing game You are required to build a simple number guessing game where the computer randomly selects a number and the user has to guess it. The user will be given a limited number of chances to guess the number. If the user guesses the number correctly, the game will end, and the user will win. Otherwise, the game will continue until the user runs out of chances.
import random
import os
os.system("cls" if os.name == "nt" else "clear")

numero_correcto = random.randint(1,100)

contador = 0
print("Welcome to the Number Guessing Game!.\n I'm thinking of a number between 1 and 100.\n")
opcion=int(input("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n Select your choose: "))

match opcion :
    case 1:
                print("Great! You have selected the Easy difficulty level.")
                limite_intentos = 10
               
    case 2:
                print("Great! You have selected the Medium difficulty level.")
                limite_intentos = 5
              
    case 3:
                print("Great! You have selected the Hard difficulty level.")
                limite_intentos = 3
              

        

while contador < limite_intentos:
    intentos= int(input("Lets start the game! \n \n Enter your guess: "))
    contador+= 1 #empieza a sumar 1
    restantes= limite_intentos-contador
    if intentos == numero_correcto:
        print(f"You did it, you got it in  {contador} attemps .")
        break
    elif intentos < numero_correcto:
        print(f"Youre wrong, the number is higher than {intentos}, you have {restantes} attemps left.")
    elif intentos > numero_correcto:
        print(f"Youre wrong, the number is lower than {intentos}, you have {restantes} attemps left.")
    if contador == limite_intentos:
        print(f"Te quedaste sin intentos. El numero era {numero_correcto}")