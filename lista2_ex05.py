def  inverter(lista):
    lista_invertida = []
    for i in range(len(lista) -1, -1, -1):
        lista_invertida.append(lista[i])

    return lista_invertida

def media(lista):
    media_total = 0
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    media_total = soma / len(lista)
    
    return media_total

def contar_acima_media(lista, m):
    cont = 0
    for i in range(len(lista)):
        if lista[i] > m:
            cont += 1
    if cont == 0:
        return 'Nenhum número acima da média!'
    
    else:
        return cont


while True:
    try:
        lista =[]
        for i in range(5):
            num = int(input(f'Informe o {i + 1}° valor: '))
            lista.append(num)
        break
    except ValueError:
        print('Número inválido, apenas inteiros, tente novamente...')


invertida = inverter(lista)
media_final = media(lista)
acima_media = contar_acima_media(lista, media_final)


print(f'Lista original: {lista}')
print(f'Lista invertida: {invertida}')
print(f'Média: {media_final:.2f}')
print(f'Números acima da média: {acima_media}')
