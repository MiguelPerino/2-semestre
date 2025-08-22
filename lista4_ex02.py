dic = {}

while True:
    try:
        nomes = input('\nInforme o nome da pessoa: ')
        if nomes == 'sair':
            break

        num = int(input('Informe o número da pessoa (xx) xxxxx-xxxx: '))
        dic[nomes] = num
    except ValueError:
        print('\nEntrada imcompátivel... Tente novamente')

print('Nomes pra procurar:')
for nome in dic:
    print(nome, end = '| ')
print()
solicitacao = input('\nDigite o nome da pessoa que procura: ')

if solicitacao in dic:
    print(f'O número de {solicitacao} é : {dic[solicitacao]}')

else: 
    print('Contato não encontrado!')

