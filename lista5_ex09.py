# Faça um programa que leia as disciplinas cursadas por dois alunos
# diferentes. Cada aluno deve ter seu nome e lista de disciplinas armazenados
# em um dicionário. Depois, mostre as disciplinas em comum, as disciplinas
# exclusivas do aluno 1 e as disciplinas exclusivas do aluno 2.

def registrations():
    students = []

    for i in range(2):
        name = input(f'Informe o nome do {i+1}° aluno: ')
        quantity = int(input(f'Quantas disciplinas {name} cursa? '))

        subjects = []
        for i in range(quantity):
            subject = input(f'Digite a {i+1}° disciplina: ')
            subjects.append(subject)

        dic = {
            'name': name,
            'subjects': subjects
        }

        students.append(dic)
    return students


def venn(students):

    set1 = set(students[0]['subjects'])
    set2 = set(students[1]['subjects'])

    intersection = set1 & set2
    difference1 = set1 - set2
    diferrence2 = set2 - set1

    print(f"\nDisciplinas em comum entre {students[0]['name']} e {students[1]['name']}:")
    print(intersection if intersection else 'nenhum')

    print(f"\nDisciplinas exclusivas de {students[0]['name']}:")
    print(difference1 if difference1 else "Nenhuma")

    print(f"\nDisciplinas exclusivas de {students[1]['name']}:")
    print(diferrence2 if diferrence2 else "Nenhuma")


lista = registrations()
print(lista)
