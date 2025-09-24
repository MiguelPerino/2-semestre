# Implemente uma função definir_idade(idade) que receba um número
# inteiro representando a idade de uma pessoa. Se a idade for negativa, a
# função deve lançar uma exceção ValueError com a mensagem "Idade
# não pode ser negativa". Caso contrário, apenas retorne a idade
# recebida. 
class negativeNumberError(ValueError):
    pass

def age_definer(age):
    if age < 0:
        raise negativeNumberError('a idade não pode ser negativa')

    return age

try:
    age_user = int(input('Digite sua idade: '))
    print(f'Sua idade é: {age_definer(age_user)}')

except negativeNumberError as e:
    print(f'Erro: {e}')
except ValueError:
    print('Erro: apenas números, sem strings')
