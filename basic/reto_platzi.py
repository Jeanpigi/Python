# seleccionar cuál metodo utilizar para calcular la raiz cuadrada utilizando un switch con diccionario
menu = """Programa para calcular la raiz cuadrada con diferentes métodos.

Por favor introducir cualquiera de los siguientes valores: 
1 para enumeración, 
2 para aproximación, 
3 para búsqueda binaria.
"""


def switch():

    print(menu)
    choose = int(
        input("Selecciona un método para calcular la raiz cuadrada: "))
    if choose <= 3 | choose >= 1:
        objetivo = int(input('Escoge un número: '))

        def enumeracion(objetivo=objetivo):
            respuesta = 0
            while respuesta**2 < objetivo:
                print(respuesta)
                respuesta += 1
            if respuesta**2 == objetivo:
                print(f'La raiz cuadrada de {objetivo} es {respuesta}')
            else:
                print(f'{objetivo} no tiene raiz cuadrada exacta')

        def aproximacion(objetivo=objetivo):
            epsilon = 0.01
            paso = epsilon**2
            respuesta = 0.0
            while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
                print(abs(respuesta**2 - objetivo), respuesta)
                respuesta += paso
            if abs(respuesta**2 - objetivo) >= epsilon:
                print(f'No se encontro la raiz cuadrada del {objetivo}')
            else:
                print(f'La raiz cuadrada del {objetivo} es {respuesta}')

        def busquedaBinaria(objetivo=objetivo):
            epsilon = 0.01
            paso = epsilon**2
            bajo = 0.0
            alto = max(1.0, objetivo)
            respuesta = (alto + bajo) / 2
            while abs(respuesta**2 - objetivo) >= epsilon:
                print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
                if respuesta**2 < objetivo:
                    bajo = respuesta
                else:
                    alto = respuesta
                respuesta = (alto + bajo) / 2
            print(f'La raiz cuadrada de {objetivo} es {respuesta}')

        # switch with dictionary
        dic = {
            1: enumeracion,
            2: aproximacion,
            3: busquedaBinaria
        }

        dic.get(choose)()
    else:
        print('Opción incorrecta, por favor escribir un número del 1 al 3')


switch()
