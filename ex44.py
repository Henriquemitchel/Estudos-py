v = float(input('Qual valor do produtor? '))
fp = int(input('Qual forma de pagamento?\n\n1 se o valor for a vista dinheiro/cheque:\n2 se o valor for no debito:\n3 se o valor for em ate 2x no cartão:\n4 se o valor for em 3x ou mais no cartão: '))

dec = v * 0.10
ac = v * 0.05
c3x = v * 0.20

if fp == 1:
    print(f'O valor do produto a vista é de R${v - dec}')
elif fp == 2:
    print(f'O produtor no debito é de R${v - ac}')
elif fp == 3:
    print(f'O valor em ate 2x é de R${v}')
else:
    print(f'O valor em 3x é de R${v + c3x}')