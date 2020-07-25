def fibonacci(number):
    if number == 0 or number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


number = int(input('Escoge un número '))

print(fibonacci(number))
