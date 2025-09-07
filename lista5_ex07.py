# Faça um programa que leia os dados de n vendas realizadas em uma loja.
# Para cada venda, o usuário deve informar o nome do cliente, o produto e o
# valor da venda. Armazene os dados em uma estrutura composta. Depois,
# calcule e mostre o valor total vendido e os clientes cadastrados (sem
# repetição). 

def registrations():
    quantity = int(input('Informe a quantidade de vendas: '))

    list_client = []
    for i in range(quantity):
        client = input(f'\nVenda {i+1} - Nome: ').title()
        product = input(f'Venda {i+1} - Produto: ').title()
        price = float(input(f'Venda {i+1} - Preço: '))

        dic = {
            'client': client,
            'product':product,
            'price': price
        }
        list_client.append(dic)

    return list_client

def total(list):
    soma = 0
    set_client = set()
    for value in list:
        soma += value['price']
        set_client.add(value['client'])
    
    print(f'\nValor total vendido: R${soma:.2f}')
    for client in set_client:
        print('-', client)

clients = registrations()

total(clients)
