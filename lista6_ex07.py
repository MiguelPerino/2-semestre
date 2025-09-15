
def registrations():
    quantity = int(input('Informe a quantidade de registros de distâncias: '))

    list_cities = []
    for i in range(quantity):
        city1 = input(f'\nRegistro {i+1} - Cidade 1: ').title()
        city2 = input(f'Registro {i+1} - Cidade 2: ').title()
        distance = int(input(f'Registro {i+1} - Distância (km): '))


        list_cities.append([city1, city2, distance])

    return list_cities

def distance(list1):

    print('\nConsulta de distância:')
    c1 = input('Informe a primeira cidade: ').title()
    c2 = input('Informe a segunda cidade: ').title()

    found = False
    for value in list1:
        if c1 in value and c2 in value:
            print(f'Distância entre {c1} e {c2}: {value[2]:.1f} km')
            found = True
            break
    if not found:
        print('\nO sistema não possue a distância dessas cidades cadastrada!')

cities = registrations()

distance(cities)


        
        
