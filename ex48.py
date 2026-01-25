s = 0
q = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        q = q + 1
        s = s + c
print(f'A soma dos {q} valores é igual a: {s}')
    