vermelho = "\033[1;31m"
reset = '\033[0m'
lista = []
for i in range(5):
    while True:
        try: 
            num = int(input(f'Informe o valor do {i + 1}° número: '))
            lista.append(num)       
            break

        except ValueError:
            print(f'\n{vermelho}Número inválido, apenas inteiros, tente novamente...{reset}\n')
lista_par = []
lista_impar = []
soma_par = 0
soma_impar = 0

for i in range(len(lista)):
    if (lista[i] % 2) == 0:
        lista_par.append(lista[i])
        soma_par += 1
    if (lista[i] % 2) == 1:
        lista_impar.append(lista[i])
        soma_impar += 1
        
print()
print(f'Lista com números pares e quantidade de elementos: {lista_par}, {soma_par}')
print(f'Lista com números ímpares e quantidade de elementos: {lista_impar}, {soma_impar}')
