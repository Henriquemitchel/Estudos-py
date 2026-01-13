km = float(input('Quantos Kms foram rodados? '))
d = int(input('Quantos dias alugados? '))
p = (km*0.15) + (60*d)
print(f'O valor total a ser pago é de R${p:.2f}')