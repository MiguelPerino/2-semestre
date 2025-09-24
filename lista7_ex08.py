# Escreva uma função atribuir_nota(nota) que receba um valor de 0 a
# 10. Se a nota estiver fora desse intervalo, a função deve lançar um
# ValueError com a mensagem "Nota deve estar entre 0 e 10".
# Caso contrário, retorne a nota.

class gapGradeError(ValueError):
    pass

def assign_grade(grade):
    if grade < 0 or grade > 10:
        raise gapGradeError('Nota deve estar entre 0 e 10')

    return grade

try:
    user_grade = float(input('Digite sua nota: '))
    print(assign_grade(user_grade))
except gapGradeError as e:
    print(f'Erro: {e}')

except ValueError:
    print('Erro: penas números!')
