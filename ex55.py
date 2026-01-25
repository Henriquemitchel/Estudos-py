lista = []

for c in range (1,6):
    p = float(input(f'Qual o peso da {c}º pessoa? '))
    lista.append(p)
print(f'A pessoa mais pesado tem {max(lista)}kg')
print(f'A pessoa mais leve tem {min(lista)}kg')