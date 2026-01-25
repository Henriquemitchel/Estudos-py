from datetime import datetime

aa = datetime.now().year
ma = 0
me = 0 

for c in range (1,8):
    a = int(input(f'Em que ano a {c}º pessoa nasceu?: '))
    idade = aa - a
    if idade >= 18:
        ma = ma + 1
    else:
        me = me + 1
print(f'Ao todo {ma} pessoas são de maiores de idade.')
print(f'E {me} pessoas são menores de idade.')
