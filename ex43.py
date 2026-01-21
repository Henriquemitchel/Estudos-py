p = float(input('Digite seu peso: (Kg) '))
a = float(input('Digite sua altura: (m) '))
imc = p / (a ** 2)

if imc < 18.5:
    print(f'Seu imc é {imc:.1f}, você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é {imc:.1f}, você está com o PESO IDEAL')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é {imc:.1f}, você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print(f'Seu imc é {imc:.1f}, você está com OBESIDADE')
else:
    print(f'Seu imc é {imc:.1f}, você está com OBESIDADE MORBIDA')