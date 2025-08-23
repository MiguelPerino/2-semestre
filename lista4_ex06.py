dic =  {

    'camiseta': 39.9,
    'calça': 89.9,
    'tênis': 199.9
}

for chave, valor in dic.items():
    print(chave, valor, end = '')
    print()

produto_solicitado = input('Informe um produto para ser retirado do estoque: ').lower().strip()


removido = dic.pop(produto_solicitado, None)
if removido is not None:
    print(f'\nO produto: {produto_solicitado} com o preço de: {removido} foi removido com sucesso!')
else:
    print('\nProduto não encontrado!')


print()
print('lista atualizada: ')
for chave, valor in dic.items():
    print(chave, valor, end = '')
    print()
