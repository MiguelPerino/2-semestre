

a = input('Digite os números do conjunto A (separados por espaço): ').split()
b = input('Digite os números do conjunto B (separados por espaço): ').split()

set_a = set()
for value in a:
    set_a.add(int(value))

set_b = set(int(value) for value in b)

union = set_a.union(set_b)
intersection = set_a.intersection(set_b)
difference_a_b = set_a.difference(set_b)
difference_b_a = set_b.difference(set_a)
symmetric_difference = set_a.symmetric_difference(set_b)

print('União:', sorted([value for value in union]))
print('Interseção:', sorted([value for value in intersection]))
print('Diferença A - B:', sorted(value for value in difference_a_b))
print('Diferença B - A:', sorted(value for value in difference_b_a))
print('Diferença simétrica:', sorted(value for value in symmetric_difference))
