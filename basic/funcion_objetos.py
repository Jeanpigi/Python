
def multiplicar_por_dos(number):
    return number * 2


def sumar_por_dos(number):
    return number + 2


def aplicar_operacion(funcion, numbers):
    resultados = []
    for number in numbers:
        resultado = funcion(number)
        resultados.append(resultado)
    print(resultados)


numbers = [1, 2, 3]
aplicar_operacion(multiplicar_por_dos, numbers)
aplicar_operacion(sumar_por_dos, numbers)


# funciones en expresiones
def sumar(numero1, numero2): return numero1 + numero2


print(sumar(2, 3))
