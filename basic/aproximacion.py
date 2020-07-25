# Aproximación de soluciones

# similar a enumeración exhaustiva, pero no necesita una respuesta exacta
# podemos aproximar soluciones con un margen de error que llamaremos epsilon

# para ser más preciso se puede pero tiene un costo y es la velocidad en el caso de cambiar epsilon a 0.001 o 0.0001 se va tardar más para dar la respuesta

objetivo = int(input('Escoge un número: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

# el abs nos devuelve un valor absoluto
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso


if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada del {objetivo}')
else:
    print(f'La raiz cuadrada del {objetivo} es {respuesta}')
