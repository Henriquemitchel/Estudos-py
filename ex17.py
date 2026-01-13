import math

#A soma dos quadrados dos catetos é igual a raiz quadrada da hiopotenusa
co = float(input('Qual comprimento do cateto oposto? '))
ca = float(input('Qual comprimento do cateto adjacente? '))
# hi = (co**2 + ca**2) ** (1/2)
hi = math.hypot(co,ca)
# hi = math.sqrt(co**2 + ca**2)
print(f'A soma de {co:.2f} + {ca:.2f} é igual a {hi:.2f}')
