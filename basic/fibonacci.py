# función para realizar fibonacci

number = int(input('Escribe un número: '))


def fibonacci(number):
    initialNumber = 0
    finalNumber = 1

    if number < 0:
        print('Incorrect input')
    elif number == 0:
        print(f'El valor es: {initialNumber}')
    elif number == 1:
        print(f'El valor es: {finalNumber}')
    else:
        for i in range(2, number):
            total = initialNumber + finalNumber
            initialNumber = finalNumber
            finalNumber = total
            print(finalNumber)
        print(f'El valor del número {number} es {finalNumber}')


# Corriendo el programa
fibonacci(number)
