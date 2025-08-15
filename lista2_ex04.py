
def somente_unicos(lista):
    lista_nova = []
    for i in range(len(lista)):
        cont = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                cont += 1

        if cont == 1:
            lista_nova.append(lista[i])
    return lista_nova


while True:
    try:
        lista = []
        for i in range(5):
            num = int(input(f'Informe o {i + 1}° número: '))
            lista.append(num)
        break
    except ValueError:
        print('Número inválido, apenas inteiros, tente novamente...')

lista_atualizada = somente_unicos(lista)
print(lista_atualizada)

