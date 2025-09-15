def registrations():

    while True:
        try:
            qnt = int(input('Quantos compromissos deseja cadastrar: '))
            break
        except ValueError:
            print('Entrada incompatível, tente novamente...')

    commitment = []
    for i in range(qnt):
        date = input(f'\nCompromisso {i + 1} - Data: ').strip()
        hour = input(f'Compromisso {i + 1} - Hora: ').strip()
        description = input(f'Compromisso {i + 1} - Descrição: ').strip()

        dic = {
            'date': date,
            'hour': hour,
            'description': description
        }

        commitment.append(dic)

    return commitment

def organized_print(commitments):

    print(f'\nTodos os compromissos: ')
    for c in commitments:
        print(f'-{c['date']} {c['hour']} | {c['description']}')

    
    search_date = input('Buscar por data: ')
    print(f'\nCompromissos em {search_date}:')
    for c in commitments:
        if c['date'] == search_date:
            print(f'- {c['hour']} | {c['description']}')
    
    dates_set = set()
    print('\nDatas sem repetição: ')
    for c in commitments:
        dates_set.add(c['date'])
    for date in dates_set:
        print('-', date)
    
    remove_commitment = input('Informe o compromisso que deseja exlcuir (ou deixe vazio para pular): ')
    if remove_commitment != '':
        for c in commitments:
            if c['description'] == remove_commitment:
                commitments.remove(c)
                print('Compromisso removido.')
                break
            else:
                print('Compromisso não encontrado.')
    
    for c in commitments:
        print(f'-{c['date']} {c['hour']} | {c['description']}')


organized_print(registrations())
