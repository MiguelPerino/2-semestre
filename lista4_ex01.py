dic = {
    'gato': 'cat',
    'cachorro': 'dog',
    'casa': 'house',
    'pessoa': 'person' 
}

palavra = input('Informe a palavra em português para ver a tradução: ').lower().strip()


if palavra not in dic:

    print('Não encontrado')

else:
    print(f'A tradução é: {dic[palavra]}')
