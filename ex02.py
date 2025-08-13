lista = []

for i in range(5):
    num = int(input(f'Informe o {i + 1}° número: '))
    lista.append(num)

lista_nova = []

for i in range(len(lista)):
    if lista[i] not in lista_nova:
        lista_nova.append(lista[i])

print(lista_nova)



lista = []

for i in range(5):
    num = int(input(f'Informe o {i + 1}° número: '))
    lista.append(num)

lista_1 = []
for i in range(len(lista)):
    lista_1.append(lista[i])


lista_nova = []
igual = True
for i in range(len(lista)):
    for j in range(len(lista_1)):
        if lista[i] == lista_1[j]:
            igual = False

    if igual == True:
        lista_nova.append(lista[i])
print(lista_nova)
