# Faça um programa que permita cadastrar as distâncias entre cidades. O
# usuário deve informar quantos registros deseja cadastrar e, para cada
# registro, digitar o nome da primeira cidade, o nome da segunda cidade e a
# distância entre elas. Armazene os dados em uma estrutura composta.
# Depois, permita que o usuário digite o nome das duas cidades e mostre a
# distância cadastrada entre elas

def registrations():
    quantity = int(input('Informe a quantidade de registros de distâncias: '))

    list_cities = []
    for i in range(quantity):
        city1 = input(f'\nRegistro {i+1} - Cidade 1: ').title()
        city2 = input(f'Registro {i+1} - Cidade 2: ').title()
        distance = int(input(f'Registro {i+1} - Distância (km): '))

        dic = {
            'city1': city1,
            'city2': city2,
            'distance': distance
        }
        list_cities.append(dic)

    return list_cities

def distance(list1):

    print('\nConsulta de distância:')
    c1 = input('Informe a primeira cidade: ')
    c2 = input('Informe a segunda cidade: ')

    for value in list1:
        if value['city1'] == c1 and value['city2'] == c2:
            print(f'Distância entre {c1} e {c2}: {value['distance']:.1f} km')
    else:
        print('\nO sistema não possue a distância dessas cidades cadastrada!')

cities = registrations()

distance(cities)


        
        
