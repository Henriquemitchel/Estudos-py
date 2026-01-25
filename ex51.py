pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
ene = pt + (10 - 1) * r

print('Os 10 primeiros termos da PA são: ')
for c in range (pt, ene + 1, r):
    print(c, end= ' - ')
    # pt = pt + r
print('Acabou')