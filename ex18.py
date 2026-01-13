from math import radians,sin,cos,tan

a = float(input('Qual o valor do angulo? '))
# rad = radians(a)

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print(f'O seno de {a} é {s:.2f} \nO cosseno de {a} é {c:.2f} \nA tangente de {a} é {t:.2f}')


