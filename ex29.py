v = float(input('Qual a velociadade do carro? '))
m = (v - 80) * 7
if v > 80:
    print(f'Voce excedeu o limite de velocidade de 80km/h e foi multado.')
else:
    print(f'Voce está dentro da velocidade permitida')
    
if v > 80:
    print(f'O valor da multa é R${m:.2f}')
  