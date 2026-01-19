from datetime import datetime

an = int(input('Em que ano você nasceu? '))
aa = datetime.now().year
id = aa - an

if id < 18:
    print(f'Você tem {id} anos. Ainda vai se alistar no exército. ')
elif id == 18:
    print(f'Você tem {id} anos. É hora de se alistar no exército. ')
else:
    print(f'Você tem {id} anos. Já passou do tempo de se alistar no exército. ')