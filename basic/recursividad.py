# factorial

def factorial(number):
    """Calcula el factorial de number

    number int > 0
    return number!
    """
    print(number)
    if number == 1:
        return 1
    return number * factorial(number - 1)


number = int(input('Escribe un entero '))

print(factorial(number))
