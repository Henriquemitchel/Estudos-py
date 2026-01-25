n = int(input('Digite um numero: '))

tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[0;32m', end = ' ')
        tot = tot + 1
    else:
        print(f'\033[0;31m', end = ' ')
    print(c, end = ' ')
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes.')
if tot == 2:    
    print(f'Por isso ele É PRIMO!')
else:
    print(f'Por isso ele NÃO É PRIMO!')
