# Implemente duas exceções personalizadas: SaldoInsuficienteError e
# ValorInvalidoError, ambas herdando de Exception. Em seguida, crie
# a função sacar(saldo, valor) que recebe o saldo atual de uma conta e
# o valor de um saque. A função deve retornar o saldo atualizado quando o
# saque for válido. Se o valor do saque for menor que zero, a função deve
# lançar ValorInvalidoError com a mensagem "Valor do saque não
# pode ser negativo". Se o valor do saque for maior que o saldo
# disponível, a função deve lançar SaldoInsuficienteError com a
# mensagem "Saldo insuficiente para realizar o saque".


class insuficientBalanceError(Exception):
    pass

class invalidValueError(Exception):
    pass


def withdraw(balance, value):
    if value < 0:
        raise invalidValueError("Valor do saque não pode ser negativo.")
    if value > balance:
        raise insuficientBalanceError("Saldo insuficiente para realizar o saque.")

    return balance - value

try:
    print(withdraw(100,60))
    # print(withdraw(100, -5))
    print(withdraw(50, 80))
    print(withdraw(100, -5))
except (insuficientBalanceError, invalidValueError) as e:
    print(f'Erro: {e}')
# except invalidValueError as e:
#     print(f'Erro: {e}')
