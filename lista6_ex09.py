def registrations():

    while True:
        try:
            qnt = int(input('Quantos produtos no cadastro: '))
            break
        except ValueError:
            print('Entrada incompatível, tente novamente...')

    products = []
    for i in range(qnt):
        product_name = input(f'\nProduto {i + 1} - Nome: ').strip()
        price = float(input(f'Produto {i + 1} - Preço: '))
        quantity = int(input(f'Produto {i + 1} - Quantidade em estoque: '))

        dic = {
            'name': product_name,
            'price': price,
            'quantity': quantity
        }

        products.append(dic)

    return products


def items_sold(products):

    while True:
        try:
            qnt = int(input('Quantos itens serão comprados: '))
            break
        except ValueError:
            print('Entrada incompatível, tente novamente...')

    sold_products = []
    for i in range(qnt):
        product_name = input(f'\nCompra {i + 1} - Nome: ').strip()
        
        product_found = False
        for p in products:
            if product_name == p['name']:
                product_found = True
                while True:
                    try:
                        quantity = int(input(f'Produto {i + 1} - Quantidade a comprar: '))
                        if quantity > p['quantity']:
                            print('Quantidade insuficiente em estoque')
                        else:
                            break
                    except ValueError:
                        print('Entrada incompatível, tente novamente...')

                dic = {
                    'name': product_name,
                    'quantity': quantity
                }
                sold_products.append(dic)                
                print(f'\033[0;32mItem registrado\033[0m.')
                break

        if not product_found:
            print('Produto não cadastrado')


    return sold_products


def organized_print(products, sold_products):

    total_value = 0
    for sp in sold_products:
        for p in products:
            if sp['name'] == p['name']:
                total_value += p['price'] * sp['quantity']
                p['quantity'] = p['quantity'] - sp['quantity']

    print(f'\nValor total da compra: R${total_value:.2f}')

    print('Estoque atualizado: ')
    for product in products:
        print(f"{product['name']}: {product['quantity']} un | R${product['price']:.2f}")


products = registrations()
sold_products = items_sold(products)
organized_print(products, sold_products)
