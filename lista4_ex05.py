
dicionario_total = {}

while True:
    try: 
        letras_chave = input('\nInforme uma letra para ser a chave do dicionário (ou digite sair quando nao quiser adicionar mais letras): ')
        if letras_chave == 'sair':
            break
        num = float(input('Informe um número para ser o valor: '))

        dicionario_total[letras_chave] = num
    
    except ValueError:
        print('Entrada incompátivel... Tente novamente!')

# for chave, valor in dicionario_total.items():
#     print(chave, valor)

soma = 0
for valor in dicionario_total.values():
    soma += valor
    
print()
print(f'A soma entre os números digitados é: {soma:.2f}')
