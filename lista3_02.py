# Crie uma tupla com os números de 1 a 10.
#  - Exiba apenas os três primeiros elementos.
#  - Exiba apenas os números pares. 

tupla = tuple(range(1, 11))

print(tupla)
print(tupla[:3])

for i in range(len(tupla)):
    if tupla[i] % 2 == 0:
        print(f'{tupla[i]}', end = f'{'':>1-} ')
