# Faça um programa que leia os dados de n funcionários, pedindo nome, cargo
# e salário. Armazene os dados em uma lista de dicionários e, ao final, mostre
# o total gasto com salários e o conjunto de cargos únicos cadastrados.

def registrations():
    quantity = int(input('Informe a quantidade de funcionários: '))

    list_employees = []
    for i in range(quantity):
        employee = input(f'\nFuncionário {i+1} - Nome: ').title()
        position = input(f'Funcionário {i+1} - Cargo: ').title()
        salary = float(input(f'Funcionário {i+1} - Salário: '))

        dic = {
            'employee': employee,
            'position': position,
            'salary': salary
        }
        list_employees.append(dic)

    return list_employees

def total(list1):
    soma = 0
    cargo = set()
    for value in list1:
        soma += value['salary']
        cargo.add(value['position'])
    
    print(f'\nTotal gasto com salários: R${soma:.2f}')
    
    print('\nCargos cadastrados: ')
    for position in cargo:
        print('-', position)

employees = registrations()
total(employees)
