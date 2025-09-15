def registrations():

    while True:
        try:
            qnt = int(input('Quantas vendas? '))
            break
        except ValueError:
            print('Entrada incompatível, tente novamente...')
    
    clients = []
    for i in range(qnt):
        name = input(f'\nVendas {i + 1} - Cliente: ')
        product = input(f'Vendas {i + 1} - Produto: ')
        price = float(input(f'Vendas {i + 1} - Valor: '))

        dic = {
            'name': name,
            'product': product,
            'price': price
        }

        clients.append(dic)
    return clients

def calculation(clients):
    total_price = 0
    for client in clients:
        total_price += client['price']
    
    set_client = set()
    for client in clients:
        set_client.add(client['name'])
    
    total_clients = []
    for client in set_client:
        total_price_client = 0
        for product in clients:
            if product['name'] == client:
                total_price_client += product['price']
        total_clients.append((total_price_client, client))
    
    biggest_spend = total_clients[0]
    for c in total_clients:
        if c[0] > biggest_spend[0]:
            biggest_spend = c

    print(f'\nValor total vendido: R${total_price:.2f}')
    print('\nClientes: ')
    for client in set_client:
        print('-', client)
    
    print('\nTotal por cliente:')
    for value in total_clients:
        print(f'- {value[1]}: R${value[0]:.2f}')

    print(f'\nCliente que mais gastou: {biggest_spend[1]} - R${biggest_spend[0]:.2f}')

calculation(registrations())
