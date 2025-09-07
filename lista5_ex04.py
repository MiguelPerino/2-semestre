# Faça um programa que leia n pares de dados representando a matrícula de
# alunos em disciplinas. Cada matrícula deve ser digitada no formato nome do
# aluno e nome da disciplina. Armazene cada matrícula como uma tupla
# (aluno, disciplina) e insira em um conjunto. Mostre ao final todas as
# matrículas sem repetição. 


def registration():
    quantity = int(input('Informe a quantidade de matrículas: '))
    registrations = set()
    for i in range(quantity):
        name = input(f'Digite o nome do {i+1}° aluno: ').strip()
        subject = input(f'Informe a disciplina do {name}: ').strip()

        student = (name, subject)
        registrations.add(student)

    print("\n--- Matrículas sem repetição ---")
    for aluno, disciplina in registrations:
        print(f"Aluno: {aluno:<10} | Disciplina: {disciplina}")

registration()
