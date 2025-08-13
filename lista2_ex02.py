
def mover_zeros(lista):
    lista_1 = []
    lista_2 = []
    for i in range(len(lista)):
        if lista[i] != 0:
            lista_1.append(lista[i])
        else:
            lista_2.append(lista[i])
        
    total = lista_1 + lista_2
    return total


lista = []
for i in range(5):
    while True:
        try:
            num = int(input(f'Informe o {i + 1}° número: '))
            lista.append(num)
            break
        except ValueError:
            print('Tente novamente... apenas números inteiros')

resultado = mover_zeros(lista)
print(resultado)
