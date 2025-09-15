def registrations():

    while True:
        try:
            qnt = int(input('Quantos contatos deseja registrar: '))
            break
        except ValueError:
            print('Entrada incompatível, tente novamente...')

    contacts = []
    for i in range(qnt):
        name = input(f'\nContato {i + 1} - Nome: ').strip()
        phone = input(f'Contato {i + 1} - Telefone: ').strip()

        dic = {
            'name': name,
            'phone': phone
        }

        contacts.append(dic)

    return contacts

def organized_print(contacts):
    contact_set = set()
    print('\nNomes cadastrados')
    for name in contacts:
        print('-', name['name'])
        contact_set.add(name['name'])
    
    print(f'\nNomes(sem repetição)')
    for contact in contact_set:
        print('-', contact)

    while True:
        option_name = input('\nDigite um nome para buscar o telefone: ').strip()    

        found = False
        for contact in contacts:
            if option_name == contact['name']:
                print(f"Telefone de {option_name}: {contact['phone']}")
                found = True
                break
        if not found:
            print('Nome não encontrado.')


        change_phone = input('\nDigite um nome para alterar o telefone (ou Enter para pular): ').strip()
        if change_phone != '':
            for contact in contacts:
                if contact['name'] == change_phone:
                    new_number = input('Novo telefone: ')
                    contact['phone'] = new_number
                    print('Telefone alterado.')
                    break
            else:
                print('Nome não encontrado.')


        remove_contact = input('\nDigite um nome para remover (ou aperte Enter para pular): ').strip()
        if remove_contact != '':
            for contact in contacts:
                if contact['name'] == remove_contact:
                    contacts.remove(contact)
                    print('Contato removido.')
                    break
            else:
                print('Nome não encontrado.')  

        print('\nLista final dos contatos: ')
        for contact in contacts:
            print(f"- {contact['name']}: {contact['phone']}")


        option = input('\nDeseja continuar? (s/n) ').lower().strip()
        if option == 'sim' or option == 's':
            continue
        else:
            break


        
organized_print(registrations())


    
