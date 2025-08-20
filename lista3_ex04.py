# Crie uma tupla chamada animais com quatro nomes de animais. Percorra a
# tupla usando range(len(...)) e imprima cada índice e o respectivo
# animal. 

animais = ('porco', 'ovelha', 'vaca', 'boi')

for i in range(len(animais)):
    print(f'{i + 1}° animal: {animais[i]}')
