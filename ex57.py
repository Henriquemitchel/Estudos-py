while True:
    s = str(input('Digite seu sexo [M/F]: ')).lower().strip()
    if s == "m" or s == "f":
        print(f'Seu sexo é {s}')
        break
    else:
        print(f'Houve um erro na digitação. Tente novamente. ')
    