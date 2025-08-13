lista = []
for i in range(5):
    palavra = input(f'Digite a {i + 1}° palavra: ')
    lista.append(palavra)

lista_nova =[]
vogais = ['a','e','i','o','u']
maior = 0
for i in range(len(lista)):
    soma_vogal = 0
    for j in range(len(lista[i])):
        if lista[i][j] in vogais:
            soma_vogal += 1
    if soma_vogal > maior:
        maior = soma_vogal
        word_mais_vogal = lista[i]
    lista_nova.append(soma_vogal)



for i in range(len(lista)):
    print(f'\nA palavra "{lista[i]}" tem {lista_nova[i]} vogais!')


print(f'\nMaior número de vogais, palavra "{word_mais_vogal}" com {maior} vogais' )
