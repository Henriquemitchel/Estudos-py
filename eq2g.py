from math import sqrt

print('Resolvedor de equação de segundo grau da Silva')


a = float(input('Digite o valor A: '))
if a == 0:
    print('O valor do primeiro termo tem que ser maior que zero.\n')
else:
    b = float(input('Digite o valor B: '))
    c = float(input('Digite o valor C: '))      
    d = (b**2) - ((4 * a) * c)
    if d < 0:
        print('O delta é nagativo, não ha raizes')
    elif d > 0:
        x1 = (-b-sqrt(d))/(2*a)
        x2 = (-b+sqrt(d))/(2*a)
        print(x1)
        print(x2)

