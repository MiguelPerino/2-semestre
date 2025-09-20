# Solicite ao usuário dois números inteiros, calcule a divisão do primeiro pelo
# segundo e exiba o resultado apenas se nenhuma falha ocorrer, utilizando
# obrigatoriamente o bloco else; trate adequadamente a entrada não
# numérica e a tentativa de divisão por zero.

try:
    numerator = int(input('Digite o numerador: '))
    denominator = int(input('Digite o denominador: '))
    if denominator == 0:
        raise ZeroDivisionError('não é possível dividir por zero')
    else:
        print(f'Resultado: {numerator / denominator}')
except ValueError:
    print(f'Erro: você digitou um valor que não é um número inteiro')

except ZeroDivisionError as e:
    print(f'Erro: {e}')
