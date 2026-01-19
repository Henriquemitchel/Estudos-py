from datetime import datetime

ano = int(input('Qual seu ano de nascimento? '))
id = datetime.now().year - ano

if id <= 9:
    print(f'Sua idade é {id} e sua categoria é: MIRIM')
elif id <= 14:
    print(f'Sua idade é {id} e sua categoria é: INFANTIL')
elif id <= 19:
    print(f'Sua idade é {id} e sua categoria é: JUNIOR')
elif id == 20:
    print(f'Sua idade é {id} e sua categoria é: SENIOR')
else:
    print(f'Sua idade é {id} e sua categoria é: MASTER')