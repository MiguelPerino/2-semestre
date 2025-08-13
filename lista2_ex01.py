'''Crie uma função quantos_maiores(lista, limite) que receba uma lista de
números e um valor limite, e retorne quantos números da lista são maiores
que esse limite.
No programa principal, leia 8 números, armazene-os em uma lista, depois
leia o valor limite, chame a função e exiba o resultado. '''


def quantos_maiores(lista, limite):
    soma = 0
    lista_maior =[]
    for valor in lista:
        if valor > limite:
            soma += 1
            lista_maior.append(valor)
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
print(f'A lista com os números maiores que o limitante: {qntd[0]} e a quantidade: {qntd[1]}')
