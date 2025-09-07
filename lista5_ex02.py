# Faça um programa que leia os nomes dos alunos de duas turmas diferentes.
# Primeiro, o usuário deve informar quantos alunos estão na turma 1 e digitar
# seus nomes. Depois, o usuário deve informar quantos alunos estão na turma
# 2 e digitar seus nomes. Armazene os nomes em listas e apresente cada
# turma na ordem digitada. Por último, mostre os alunos que estão nas duas
# turmas, apenas na turma 1 e apenas na turma 2

def class_a():
    while True:
        try:
            quantity = int(input('Informe a quantidade alunos na turma A: '))
            break
        except ValueError:
            print('Entrada incompatível... Tente novamente')
        
    students_a = []
    for i in range(quantity):
        name = input(f'Digite o nome do {i+1}° aluno: ')
        students_a.append(name)
    
    return students_a

def class_b():
    while True:
        try:
            quantity = int(input('Informe a quantidade alunos na turma B: '))
            break
        except ValueError:
            print('Entrada incompatível... Tente novamente')
    
    students_b = []
    for i in range(quantity):
        name = input(f'Digite o nome do {i+1}° aluno: ')
        students_b.append(name)
    
    return students_b
    
def show_all(list_a, list_b):
    print('Alunos da Turma A')
    for i in range(len(list_a)):
        print(f'{i+1}° aluno: {list_a[i]}')    

    print('\nAlunos Turma B')
    for i in range(len(list_b)):
        print(f'{i+1}° aluno: {list_b[i]}')

    set_a = set(list_a)
    set_b = set(list_b)

    print("\n--- Alunos em ambas as turmas ---")
    both = set_a.intersection(set_b)
    if both:
        for student in both:
            print('-', student)
    else: 
        print('Nenhum')

    print("\n--- Apenas na Turma A ---")
    only_a = set_a.difference(set_b)
    if only_a:
        for student in only_a:
            print('-', student)
    else:
        print('Nenhum')

    print("\n--- Apenas na Turma B ---")
    only_b = set_b.difference(set_a)
    if only_b:
        for student in only_b:
            print('-', student)
    else:
        print('Nenhum')

turma_a = class_a()
turma_b = class_b()

show_all(turma_a, turma_b)
