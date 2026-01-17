n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O numero {n1} é maior.')
elif n2 > n1:
    print(f'O numero {n2} é maior.')
elif n1 == n2:
    print(f'Não existe maior valor {n1} e {n2} são iguais.')