from random import randint
from random import choice

i = ['Pedra', 'Papel', 'Tesoura']
e = int(input('\n[ 0 ] Pedra:\n[ 1 ] Papel:\n[ 2 ] Tesoura:\nQual você escolhe? '))
print('')
# p = 'pedra'
# pp = 'papel'
# t = 'tesoura'
em = randint(0, 2)

# lista = [p,pp,t]
# em = choice(lista)

if e == em:
    print(f'Escolheram a mesma coisa, {i[e]}.\n\033[0;36mDEU EMPATE\033[m')
elif e == 0 and em == 2 or e == 1 and em == 0 or e == 2 and em == 1:
    print(f'Jogar jogou {i[e]}\nComputador jogou {i[em]}.\n\033[0;32mJOGADOR VENCEU\033[m')
elif e == 0 and em == 1 or e == 1 and em == 2 or e == 2 and em == 0:
    print(f'Computador jogou {i[em]}\nJogador jogou {i[e]}.\n\033[0;31mCOMPUTADOR VENCI\033[m')
else:
    print('Escolha invalida, tente novamente.')



