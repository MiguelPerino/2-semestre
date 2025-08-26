funcionarios = []

contador = 1
while True:    
    try: 
        nome_digitado = input(f'Informe o nome do {contador}° funcionário: ')
        
        if nome_digitado.lower() == 'sair':
            break
        cargo_digitado = input(f'Informe o cargo do(a) {nome_digitado}: ')
        salario_inicial = float(input(f'Informe o salário inicial do(a) {nome_digitado}: R$'))
        print()
        funcionario = {
            'nome': nome_digitado,
            'cargo': cargo_digitado,
            'salario': salario_inicial
        }

        funcionarios.append(funcionario)
        contador += 1

    except ValueError:
        print('Entrada incompátivel...')

print('\nLISTA DOS FUNCIONÁRIOS:')
for valor in funcionarios:
    print(f'Nome: {valor['nome']}, Cargo: {valor['cargo']}, Salário: R${valor['salario']:.2f}')
    

atualizar = input('\nDeseja atualizar o salário de algum funcionário(s/n)? ').lower()
print()

if atualizar == 'sim' or atualizar == 's':
    funcionario_atualizado = input('Qual funcionário? ').lower()
      
    encontrado = False
    for dicionario_individual in funcionarios:
        if dicionario_individual['nome'] == funcionario_atualizado:
            salario_novo = float(input(f'\nInforme o novo salário de {funcionario_atualizado}: '))
            dicionario_individual['salario'] = salario_novo
            encontrado = True
            print(f'Sálario de {dicionario_individual['nome']} atualizado para R${salario_novo:.2f}!')
            break
    if not encontrado:
        print('funcionário não encontrado')

print()
print('Lista final de funcionários: ')
for func in funcionarios:
    print(f'Nome: {func['nome']}, Cargo: {func['cargo']}, Salário: R${func['salario']:.2f}')



