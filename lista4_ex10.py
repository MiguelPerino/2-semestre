dic = {}


while True:
    try:
        nome = input('Informe o nome do aluno(ou digite "sair"): ')
        if nome == 'sair':
            break
        nota = float(input('Informe a nota desse aluno: '))

        dic[nome] = nota
    except ValueError:
        print('Entrada incompátivel')


print('NOME:         |   NOTA:')
for k, v in dic.items():
    print(f'{k:<13} | {v:>6.2f}')

# maior = next(iter(dic.items()))   #da pra colocar maior = 0(mas se for negativo as notas, da erro)
# for k, valor in dic.items():
#     if valor > maior:
#         maior = valor
#         nome_maior = k
# print(f'A maior nota é {maior:.2f} do aluno: {nome_maior} ')

if dic: 
    nome_maior = max(dic, key = dic.get)
    nota_maior = dic[nome_maior]
    print(f"A maior nota é {nota_maior:.2f} do aluno: {nome_maior}")
