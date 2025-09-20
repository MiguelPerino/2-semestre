# Considere a lista ["arroz", "feijão", "macarrão", "óleo"].
# Peça ao usuário um índice e mostre o item correspondente.
# Trate entrada não numérica e índice fora da faixa.

foods = ["arroz", "feijão", "macarrão", "óleo"]

print(foods)
try:
    food = int(input('Digite o índice do item: '))
    if food <0 or food >= len(foods):
        raise IndexError('índice inexistente na lista')
    else:
        print(f'O item escolhido foi: {foods[food]}')
except ValueError:
    print(f'Erro: Você digitou um valor que não é número inteiro.')

except IndexError as e:
    print(f'Erro: {e}')
