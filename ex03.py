''') Leia oito números digitados pelo usuário e armazene-os em uma lista. Ao
final, exiba a lista original, a lista em ordem inversa, a média dos valores
digitados e, por último, a quantidade de números que estão acima da média
calculada. '''
while True:
    try:
        lista = []
        for i in range(4):
            num = float(input(f'Informe o valor do {i + 1}° número: '))
            lista.append(num) 

        tamanho = len(lista)
        print(lista)
        break
    except ValueError:
        print('\nNúmero inválido, tente novamente!')
        print()

lista_inversa = []
for i in range(tamanho -1, -1 ,-1):
    lista_inversa.append(lista[i])

print(lista_inversa)

soma = 0
for i in range(tamanho):
    soma += lista[i]

media = soma / tamanho
print(f'{media:.2f}')

soma_num = 0
for i in range(len(lista)):
    if lista[i] > media:
        soma_num += 1

if soma_num == 0:
    print('Nenhum número acima da média!')
else:
    print(soma_num)
