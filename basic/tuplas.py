my_tupla = ()

print(type(my_tupla))

my_tupla = (1, 'dos', True)

print(my_tupla[0])

# Para definir una tupla es importante que lleve una coma al final si es de un solo elemento

my_tuple = (1,)

print(type(my_tuple))

my_other_tuple = (2, 3, 4)

# para asignar los valores a otra tupla se realiza de esta forma
my_tuple += my_other_tuple

# de igual forma se pueden asignar de la siguiente manera
x, y, z = my_other_tuple
print(x, y, z)


def coordenadas():
    return (5, 4)


coordenada = coordenadas()
print(coordenada)
x, y = coordenadas()
print(x, y)
