# Leia os dados de n alunos (nome e curso). Armazene em uma lista de
# dicionários e mostre:
# • todos os alunos cadastrados;
# • o conjunto de cursos sem repetição;
# • a quantidade de alunos em cada curso


def registrations():
    students = []
    quantity = int(input('Quantos alunos: '))
    for _ in range(quantity):
        name = input('\nInforme o nome do aluno: ')
        subject = input(f'Digite o curso do {name}: ')

        dic = {
            'name': name,
            'subject': subject
        }
        students.append(dic)    

    for student in students:
        print(f"- {student['name']} ({student['subject']})")


    courses = set() 
    for value in students:
        courses.add(value['subject'])

    print(f'\nCursos cadastrados: ')
    for course in courses:          
        print('-', course)
    
    qnt_student = []
    for course in courses:
        cont = 0
        for s in students:
            if s['subject'] == course:
                cont += 1
        qnt_student.append((cont, course))

    print('\nQuantidade de alunos por curso: ')
    for qnt in qnt_student:
        print(f'- {qnt[1]}: {qnt[0]}')


registrations()

    
