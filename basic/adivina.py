import random

# Aquí esta la variable que crea un número del 1 a l 100
numeroAdivinar = random.randint(1, 100)

# Aquí te muestra el número creado con el modulo random
print(numeroAdivinar)

# Aquí se realiza la lógica para preguntar y responder si se adivina el número
while numeroAdivinar:
    print('Adivina un número del 1 al 100')
    numeroUsuario = int(input('Por favor escirbe el número: '))
    if(numeroUsuario == numeroAdivinar):
        print('')
        print('Perfecto adivinaste el número')
        break
    else:
        print('')
        print('Lo siento no es el número, prueba de nuevo')
        print('')
