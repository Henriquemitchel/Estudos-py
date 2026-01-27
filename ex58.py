from random import randint 
from time import sleep

n = randint(0,10)

print('Vou pensar em um numero de 0 a 10, tente adivinhar.')
print('Pensando...')
sleep(1)

tp = 0

while True:
    e = int(input('Qual numero pensei? '))
    if n == e:
        print(f'Correto, o numero foi {n}!\nVocê tentou {tp} vezes ate acertar.')
        break
    else:
        print(f'Errrado. Tente novamente.') 
        tp = tp + 1