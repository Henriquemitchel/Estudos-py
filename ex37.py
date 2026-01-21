num = int(input('Digite o número inteiro que deseja converter: '))
e = int(input('[ 1 ] Converter para BINÁRIO: \n[ 2 ] Converter para OCTAL: \n[ 3 ] Converter para HEXADECIMAL:\nQue base de conversão você deseja? '))

if e == 1:
    print(f'O numero {num} convertido para binário é {bin(num)[2:]}')
elif e == 2:
    print(f'O numero {num} convertido para octal é {oct(num)[2:]}')
elif e == 3:
    print(f'O numero {num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print(f'{e} está fora das opções de escolha. Tente novamente.')