entrada = input('Informe uma palavra: ')

dic = {}

for i in range(len(entrada)):
    cont = 0
    for j in range(len(entrada)):

        if entrada[i] == entrada[j]:
            cont += 1

        dic[entrada[i]] = cont

for k, v in dic.items():
    if v == 1:
        print(f'A letra "{k}" se repete {v} vez')
    else:
        print(f'A letra "{k}" se repete {v} vezes')
