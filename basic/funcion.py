def add(numero1, numero2):
    total = numero1 + numero2
    return total


print(add(2, 2))


def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return print(f'{apellido} {nombre}')
    else:
        return print(f'{nombre} {apellido}')


nombre_completo('Jean Pierre', 'Arenas')
nombre_completo('Jean Pierre', 'Arenas', inverso=True)
nombre_completo(apellido='Arenas', nombre='Jean Pierre')
