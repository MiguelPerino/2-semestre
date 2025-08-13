'''Crie uma função mover_zeros_fim(lista) que receba uma lista de 12 números
inteiros e retorne uma nova lista em que todos os zeros sejam movidos para
o final, preservando a ordem relativa dos demais elementos e mantendo o
tamanho da lista original.
No programa principal, leia 12 números inteiros, armazene-os em uma lista,
chame a função e exiba o resultado.'''

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
