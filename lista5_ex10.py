# Faça um programa que leia os dados de n contatos (nome e telefone) e
# armazene em uma lista de dicionários. O programa deve (a) mostrar todos os
# nomes cadastrados; (b) mostrar todos os nomes sem repetições; e (c)
# permitir que o usuário digite um nome para exibir o telefone correspondente. 

def registrations():
    quantity = int(input('Informe a quantidade de contatos: '))

    all_contacts = []
    for i in range(quantity):
        name = input(f'\nNome {i+1} - Nome: ').title()
        number = input(f'Telefone {i+1} - Telefone: ').title()

        dic = {
            'name': name,
            'number': number,
        }
        all_contacts.append(dic)

    return all_contacts

def all_names(contacts):

    set_name = set()
    print('\nNomes cadastrados')
    for name in contacts:
        print('-', name['name'])
        set_name.add(name['name'])
    
    print('\nNomes únicos')
    for name in set_name:
        print('-', name)
    
    name_number = input('\nDigite um nome para buscar o telefone: ').title().strip()
    for number in contacts:
        if number['name'] == name_number:
            print(f'Telefone de {name_number}: {number['number']}')

contacts = registrations()
all_names(contacts)
