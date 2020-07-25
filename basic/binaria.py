# Busqueda Binaria

# Cuando la respuesta se encuentra en un conjunto ordenado, podemos utilizar búsqueda binaria
# Es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración

objetivo = int(input('Escoge un número: '))
epsilon = 0.0001
# bajo es el limite inferior
bajo = 0.0
# alto es el limite superior
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
