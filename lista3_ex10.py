def estatistica(lista):
    maior = lista[0]
    menor =lista[0]
    soma = 0
    for valor in lista:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        else:
            soma += valor
            media = soma / len(lista)
    return (menor, maior, media)


lista = []
for i in range(5):
    num = int(input(f'Informe o {i+ 1}° número: '))
    lista.append(num)

menor, maior, media = estatistica(lista)

print(f'Menor número: {menor}')
print(f'Maior número: {maior}')
print(f'Média entre eles: {media:.2f}')
