# Crie uma função dividir(a, b) que devolva o resultado da divisão a /
# b. Caso b seja zero, a função deve lançar a exceção ZeroDivisionError
# com a mensagem "Denominador não pode ser zero".

def division(a, b):
    if b == 0:
        raise ZeroDivisionError('Denominador não pode ser zero')
    return a / b

try:
    a = int(input('Informe o numerador: '))
    b = int(input('Informe o denominador: '))
    print(division(a, b))
except ZeroDivisionError as e:
    print(f'Erro: {e}')

