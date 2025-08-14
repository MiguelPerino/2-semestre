def soma_entre(x, y):

    soma = 0
    if x <= y:
        for i in range(x, y + 1):
            soma += i
    
    else:
        for i in range(x, y -1, - 1):
            soma += i
    
    return soma

while True:
    try:
        x = int(input('Informe o primeiro número limitante: '))
        y = int(input('Informe o segundo número limitante: '))
        break   

    except ValueError:
        print('Número inválido, tente novamente...\n')

soma_total = soma_entre(x,y)
print(soma_total)
