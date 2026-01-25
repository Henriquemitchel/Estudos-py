s = 0
cont = 0
for c in range (1,7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        cont = cont + 1
        s = s + n
print(f'A soma dos {cont} valores PARES é de: {s}')    