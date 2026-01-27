s = 0
q = 0
g = 1

while True:
    n = int(input(f'Digite o {g}º numero ou 999 para parar: '))
    if n == 999:
        break
    s = s + n 
    g = g + g
    q = q + 1
print(f'O total de numeros digitados foi {q} e a soma deles foi {s}')
