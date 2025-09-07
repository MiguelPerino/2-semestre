# Faça um programa que cadastre os dados de n produtos, informando nome e
# preço. Em seguida, o usuário deve digitar os nomes dos produtos comprados
# por um cliente e o programa deve mostrar o valor total da compra. 

def cadastro():
    list_products = []
    quantity = int(input('Informe a quantidade de produtos: '))
    for i in range(quantity):
        name= input(f'Digite o nome do {i+1}° produto: ')
        price = float(input('Informe o preço do produto: R$'))
    
        dic = {
            'name': name,
            'price': price
        }
        list_products.append(dic)
    return list_products

def purchased_items():
    list_purchased_items = []
    quantity = int(input('\nInforme a quantidade de produtos comprados: '))
    for i in range(quantity):
        product_name = input(f'Digite o nome do {i+1}° produto: ')
        list_purchased_items.append(product_name)
    return list_purchased_items

def total(list1, list2):
    soma = 0
    not_founded = []
    for items in list2:
        found = False
        for value in list1:
            if items == value['name']:
                soma += value['price']
                found = True
                break
        if not found:
            not_founded.append(items)
    
    print(f'\nValor total da compra: R${soma:.2f}')

    if not_founded:
        print('\nItens não encontrados no cadastro:')
        for value in not_founded:
            print('-', value)
    else:
        print('Todos os produtos foram encontrados no cadastro!')


cadastro_product = cadastro()
sale = purchased_items()
total(cadastro_product, sale)

    
