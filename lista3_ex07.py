#  Crie uma tupla com números inteiros, incluindo repetições. Peça ao usuário
# um número e mostre quantas vezes ele aparece na tupla

from random import randint
lista = []
for _ in range(10):
    lista.append(randint(1, 10))
tupla = tuple(lista)

print(tupla)

while True:
    try:
        num = int(input('Informe um número: '))
        break
    except ValueError:
        print('Apenas números inteiros...')
cont = 0
for i in range(len(tupla)):
    if num == tupla[i]:
        cont += 1
print(f'Seu número aparece: {cont} vezes.')

# tupla = tuple((randint(1, 10)) for _ in range(10))
# print(tupla)
