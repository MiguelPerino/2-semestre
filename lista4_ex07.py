dic1 = {}
dic2 = {}

contador1 = 1
while True:
    chave = input(f'\nInforme a {contador1}° chave do dic 1 (ou digite sair): ')
    if chave == 'sair':
        break
    contador1 += 1
    valor = input('Informe o valor: ')
    dic1[chave] = valor


contador2 = 1
while True:
    chave2 = input(f'\nInforme a {contador2}° chave do dic 2(ou digite sair): ')
    if chave2 == 'sair':
        break
    contador2 += 1
    valor2 = input('Informe o valor: ')
    dic2[chave2] = valor2

print(f'Dicionário 1: {dic1}')

print(f'Dicionário 2: {dic2}')

dic1.update(dic2)
print(f'Dicionário concatenado: {dic1}')
