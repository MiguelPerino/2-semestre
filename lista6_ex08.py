def registrations():
    students = []
    for i in range(2):
        name = input(f'Nome do {i+1}° aluno: ')
        while True:
            try:
                subjects_qnt = int(input(f'Informe quantas disciplinas {name} cursa: '))
                break
            except ValueError:
                print('Entrada incompatível, tente novamente...')
        
        subjects = set()
        for i in range(subjects_qnt):
            subject = input(f'Digite a {i+1}° disciplina de {name}: ').strip()
            subjects.add(subject)

        dic = {
            'name': name,
            'subjects': subjects
        }
        students.append(dic)

    return students

def organized_print(students):
    if not students:
        print('Nnenhum aluno registrado')
        return
    
    student_1 = students[0]
    student_2 = students[1]

    intersection = student_1['subjects'].intersection(student_2['subjects'])
    print('Disciplinas em comum: ')
    for s in intersection:
        print('-', s)

    difference_a_b = student_1['subjects'].difference(student_2['subjects'])
    print(f"\nSomente {student_1['name']}:")
    for s in difference_a_b:
        print('-', s)

    difference_b_a = student_2['subjects'].difference(student_1['subjects'])
    print(f"\nSomente {student_2['name']}:")
    for s in difference_b_a:
        print('-', s)

    quantity = [len(intersection), len(student_1['subjects']), len(student_2['subjects'])]
    print('\nQuantidades:')
    print(f'Em comum: {quantity[0]}')
    print(f'Exclusivas de {student_1['name']}: {quantity[1]}')
    print(f'Exclusivas de {student_2['name']}: {quantity[2]}')

organized_print(registrations())
