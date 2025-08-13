def quantos_maiores(lista, limite):
    soma = 0
    lista_maior =[]
    for valor in lista:
        if valor > limite:
            soma += 1
            lista_maior.append(valor)
    if len(lista_maior) == 0:
        return ['A lista está vazia', soma]
    return [lista_maior, soma]


lista = []
for i in range(5):
    while True:
        try:
            num = int(input(f'Informe o {i+ 1}° número: '))
            lista.append(num)
            break
        except ValueError:
            print('\nNúmero inválido, apenas inteiros...\n')

limitante = int(input('\nInforme o valor limitante: '))

qntd = quantos_maiores(lista, limitante)
print(lista)
print(f'A lista com os números maiores que o limitante: {qntd[0]} e a quantidade é: {qntd[1]}')
