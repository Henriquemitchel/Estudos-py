n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print(f'Sua media foi {med} e você foi \033[0;31mREPROVADO\033[m')
elif med > 5 and med < 6.9:
    print(f'Sua media foi {med} e você está de \033[0;36mRECUPERAÇÃO\033[m')
else:
    print(f'Sua media foi {med} e você foi \033[0;32mAPROVADO\033[m')
