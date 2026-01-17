an = int(input('Qual ano voce nasceu? '))
aa = an - 2026
if aa < 18:
    print('Voce ainda vai se alistar no exercito')
elif aa == 18:
    print('É hora de se alistar no exercito')
else:
    print('Ja passou do tempo de se alistar no exercito')