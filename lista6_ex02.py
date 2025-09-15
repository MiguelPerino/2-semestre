# Leia os dados de n funcionários (nome, cargo, salário). Mostre:
# • total gasto com salários;
# • salário médio, maior e menor;
# • cargos sem repetição;
# • o funcionário com maior salário.


def registrations():
    while True:
        try:
            qnt = int(input('Quantos funcionários? '))
            break
        except ValueError:
            print('Tente novamente, entrada incompatível...')
    

    employees = []
    for i in range(qnt):
        name = input(f'\nFuncionário {i + 1} - Nome: ')
        position = input(f'Funcionário {i + 1} - Cargo: ')
        salary = float(input(f'Funcionário {i + 1} - Salário: '))

        dic = {
            'name': name,
            'position': position,
            'salary': salary
        }

        employees.append(dic)
    return employees

def calculation(employees):
    total_sum = 0
    biggest = employees[0]['salary']
    smallest = employees[0]['salary']
    for value in employees:
        salary = value['salary']
        total_sum += salary

        if salary > biggest:
            biggest = salary
        
        if salary < smallest:
            smallest = salary
    

    media = total_sum / len(employees)

    set_position = set()
    for position in employees:
        set_position.add(position['position'])
    

    print(f'total salário: R${total_sum:.2f}')
    print(f'Salário médio: R${media:.2f}')
    print(f'Maior salário: R${biggest:.2f}')
    print(f'Menor salário: R${smallest:.2f}') 

    print('\nCargos: ')
    for position in set_position:
        print('-', position)
calculation(registrations())
