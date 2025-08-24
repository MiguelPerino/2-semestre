estoque = {
    "camiseta": 25,
    "calça": 18,
    "tênis": 12,
    "boné": 30,
    "jaqueta": 7,
    "meias": 50,
    "moletom": 10,
    "saia": 15,
    "shorts": 20,
    "óculos": 8
}

print("\nProduto            | Quantidade")
print("-" * 31)
for k, v in estoque.items():
    print(f"{k:<18} | {v:>10}")


while True:
    entrada = input('Digite o nome do produto vendido (ou digite "sair"): ').lower().strip()
    if entrada == 'sair':
        print('\nSaindo do programa... até logo!')
        break

    if entrada in estoque:
        if estoque[entrada] > 0:
            estoque[entrada] -= 1
            print(f'\n\033[32mVenda realizada\033[0m! Novo estoque: {estoque[entrada]}')
        else:
            print(f'\n\033[31mSem estoque de {entrada}!\033[0m')

    else:
        print('\n\033[31mProduto não encontrado\033[0m!')

    
    print("\nProduto            | Quantidade")
    print("-" * 31)
    for k, v in estoque.items():
        print(f"{k:<18} | {v:>10}")

