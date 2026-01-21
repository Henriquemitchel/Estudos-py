from datetime import datetime

an = int(input('Em que ano você nasceu? '))
aa = datetime.now().year
id = aa - an

if id < 18:
    s = 18 - id
    a = aa + s
    print(f'Você tem {id} anos. Ainda faltam {s} anos para se alistar.\nSeu alistamento será em {a}.  ')
elif id == 18:
    print(f'Você tem {id} anos. É hora de se alistar no exército. ')
else:
    s = id - 18
    a = aa - s
    print(f'Você tem {id} anos. Já deveria ter se alistado a {s} anos.\nSeu alistamento foi em {a}. ')