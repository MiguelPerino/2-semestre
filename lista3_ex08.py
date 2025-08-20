#  Dada a tupla vogais = ('a', 'e', 'i', 'o', 'u'), peça ao usuário
# uma vogal e exiba em qual posição ela está.

vogais = ('a', 'e','i','o','u')

vogal = input('Informe uma vogal: ')
 
for i in range(len(vogais)):
    if vogal == vogais[i]:
        print(f'A posição da vogal é a {i}°')

