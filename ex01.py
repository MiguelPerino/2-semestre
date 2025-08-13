# Leia doze números inteiros e armazene-os em uma lista. Construa e exiba
# uma nova lista em que todos os zeros sejam movidos para o final,
# preservando a ordem relativa dos demais elementos e mantendo o tamanho
# da lista original. 

try:
    lista = []
    for i in range(8):
        num = int(input(f'Informe o {i + 1}° núm: '))
        lista.append(num)

    lista_1 = []
    lista_2 = []
    for i in range(len(lista)):
        if lista[i] != 0:
            lista_1.append(lista[i])
        else:
            lista_2.append(lista[i])
    
    total = lista_1 + lista_2
    print(total)


except ValueError:
    print('Número inválido, apenas inteiros')
