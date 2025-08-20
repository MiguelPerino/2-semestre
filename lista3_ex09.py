# Crie uma tupla chamada produto contendo as informações nome, preço e
# quantidade. Depois, exiba uma frase no formato:
# O produto <nome> custa R$<preço> e temos <quantidade> unidades em
# estoque.

produto = ('Teclado', 50.00, 10)
print(f'O produto {produto[0]} custa R${produto[1]:.2f} e temos {produto[2]} unidades em estoque!')
