from random import randint
from time import sleep

n = randint(0,5)
 
print(f'Vou pensar em um numero de 0 a 5, tente adivinhar... ')
print('Pensando... ')
sleep (3)

e = int(input('Em que numero pensei? '))

if n == e:
    print(f'O numero era {n}, você venceu! parabens!')
elif e > 5:
    print('O numero tem que ser de 1 a 5')
else:
    print(f'O numero era {n}, eu venci!')
