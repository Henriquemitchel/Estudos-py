s = int(input('Qual seu salario atual? R$'))
cores = {'verde' : '\033[32m', 'azul' : '\033[1;36m'}

if s > 1250:
    print(f'Seu salario teve um {cores ['azul']}aumento de 10%\033[m, agora seu salario é {cores ["verde"]}R${s * 0.10 + s:.2f}\033[m')
else:
    print(f'Seu salario teve um {cores ['azul']}aumento de 15%\033[m, agora seu salario é {cores ["verde"]}R${s * 0.15 + s:.2f}\033[m')