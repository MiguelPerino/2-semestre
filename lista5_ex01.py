# Faça um programa que leia os dados de n alunos. Para cada aluno, o
# usuário deve informar o nome e o curso em que ele está matriculado.
# Armazene as informações em uma lista de dicionários e, ao final, mostre
# todos os cursos cadastrados sem repetição. 

while True:
    try:
        quantity = int(input('Quantos alunos deseja cadastrar? '))
        break
    except ValueError:
        print('Apenas números inteiros, tente novamente...')

list_student = []
for i in range(quantity):
    name = input(f'Infomre o nome do {i+1}° aluno: ')
    degree = input('Informe o curso: ')
    
    student = {
        'name': name,
        'degree': degree
    }
    list_student.append(student)

conj = set()
for student in list_student:
        conj.add(student['degree'])


print('\nCursos cadastrados:')
for degree in conj:
    print('-', degree)



