from random import choice

e = str(input('Qual você escolhe:\nPedra, Papel ou Tesoura? ')).strip().lower()
p = 'pedra'
pp = 'papel'
t = 'tesoura'

lista = [p,pp,t]
em = choice(lista)

if e == em:
    print(f'Nós escolhemos a mesma coisa, {e}. \033[0;36mDEU EMPATE\033[m')
elif e == 'pedra' and em == 'tesoura' or e == 'papel' and em == 'pedra' or e == 'tesoura' and em == 'papel':
    print(f'Você escolheu {e} e eu {em}. \033[0;32mVOCÊ VENCEU\033[m')
elif e == 'pedra' and em == 'papel' or e == 'papel' and em == 'tesoura' or e == 'tesoura' and em == 'pedra':
    print(f'Eu escolhi {em} e você {e}. \033[0;31mEU VENCI\033[m')



