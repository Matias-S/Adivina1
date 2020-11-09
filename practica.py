# Este es un jueguito del tipo "adviná el número".

import random
numeroSuerte = random.randint(1, 10) # El número a ser adivinado
numeroHumor = random.randint (1, 2) # Número para determinar si adivina una o dos veces
bandera = 0 # Variable para control

print("DEBUG: NUMERO DE LA SUERTE: " + str(numeroSuerte)) #Para verificar si el programa funciona como corresponde. Comentarlas para eliminarlas
print("DEBUG: NUMERO DE HUMOR: " + str(numeroHumor))      

print("Buen día, cómo es tu nombre?")
name = input()

print("Hola " + str(name) + ", estoy pensando en un número del 1 al 10, podrás adivinar en cuál?")

for i in range (1, 3):
    while True:
        try:
            adivino = int(input()) # adivino es el número que elige el usuario
            if adivino > 10 or adivino < 1:
                print("Tenés que ingresar un número del 1 al 10!") # Vuelve a pedir un número si el usuario no entra un número del 1 al 10
                continue
            elif adivino <= 10 and adivino >=1:
                bandera = 1 # Asignamos 1 a la bandera si el dato ingresado es satisfactorio
                break            

        except ValueError:
             print("Tenés que ingresar un número, no palabras!") # Vuelve a pedir un número si el usuario entra letras
             continue

        if bandera == 1: #En el caso de que la bandera sea =1 debido a un valor ingresado correctamente, sale del ciclo y continúa el resto del programa
            break
                              
    if int(adivino) == numeroSuerte:
        print("Felicitaciones " + str(name) + ", adivinaste el número!")
        break
    else:
        print("Qué pena, ese no era el número!")
        if numeroHumor == 2:
            print("Como estoy de buen humor, voy a dejar que adivines una vez más!")
            numeroHumor = 1  #Cambiamos el valor de la variable de "Humor" para que no se repita el mensaje de arriba
            
        else:
            break

print("Volvé a jugar y probá tu suerte!")


