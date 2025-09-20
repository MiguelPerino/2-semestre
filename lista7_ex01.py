total = (input('Informe o preço total: '))
try:
    total = float(total)

    if total < 0:
        print('Erro: Não pode números negativos')

    else:
        quantity = (input('Informe a quantidade: '))
        try:
            quantity = int(quantity)
            if quantity < 0:
                print(f'Erro: Numero nao pode ser negativo')

            elif quantity == 0:
                print('Erro: Não pode ser 0')
                
            else:
                unitary_price = total / quantity
                print(unitary_price)
        except ValueError:
            print(f'Erro: Digite números válidos')

except ValueError:
    print('Erro: Digite números válidos')
