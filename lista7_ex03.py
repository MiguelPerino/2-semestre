# Tente abrir um arquivo chamado dados.txt, ler seu conteúdo e convertê-lo
# para número inteiro. Trate arquivo inexistente e conteúdo não numérico,
# exibindo mensagens adequadas

with open('text.txt', 'w') as text:
    content = text.write(input('Digite algo: '))

try:
    with open('text.txt', 'r') as text:
        read_file = text.read()

    try:
        read_content = int(read_file)
        print(f'Número lido: {read_content}')

    except ValueError:
        print(f'Erro: conteúdo do arquivo não é um número inteiro')
except FileNotFoundError:
    print('Erro: arquivo não encontrado')
