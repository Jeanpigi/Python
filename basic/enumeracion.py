# Programas numéricos

# Enumeracion exhaustiva  es enumerar todas las posibilidades que tenemos dentro de nuestra solución
# las computadoras actuales son muy rápidas, debe ser uno de los primeros algoritmos que debes tratar para solucionar un problema
# El problema a resolver tiene que ver con las raices cuadradas más cercanas

objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raiz cuadrada exacta')
