lista = []
try:
    for i in range(5):
        num = int(input(f'Informe o {i + 1}° número: '))
        lista.append(num)
except ValueError:
    print('Número inválido, apenas inteiros!')


lista_nova = []
for i in range(len(lista)):
    igual = True

    for j in range(len(lista_nova)):
        if lista[i] == lista_nova[j]:
            igual = False
            break

    if igual == True:
        lista_nova.append(lista[i])

print(lista_nova)
