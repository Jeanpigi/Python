frutas = ['manzana', 'pera', 'mango']

estudiantes = {
    'mexico': 10,
    'Colombia': 15,
    'puerto rico': 4,
}

for fruta in frutas:
    print(fruta)

for pais in estudiantes:
    print(f'Esta parte es por Pais {pais}')


for pais in estudiantes.keys():
    print(f'Esta es con una llave {pais}')

for pais in estudiantes.values():
    print(f'Esta es con un valor {pais}')

for pais in estudiantes.items():
    print(f'Esta es con items {pais}')
