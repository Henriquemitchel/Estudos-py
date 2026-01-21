from datetime import datetime

ano = int(input('Qual seu ano de nascimento? '))
id = datetime.now().year - ano

if id <= 9:
    print(f'Sua idade é {id} anos\nCategoria: MIRIM')
elif id <= 14:
    print(f'Sua idade é {id} anos\nCategoria: INFANTIL')
elif id <= 19:
    print(f'Sua idade é {id} anos\nCategoria: JUNIOR')
elif id <= 25:
    print(f'Sua idade é {id} anos\nCategoria: SÊNIOR')
else:
    print(f'Sua idade é {id} anos\nCategoria: MASTER')