d = float(input('Qual é a distancia da viagem? '))
# vc = d*0.50
# vl = d*0.45

if d <= 200:
    print(f'Essa foi uma viagem curtar, o valor cobrado será: R${d*0.50:.2f}')
else:
    print(f'Essa foi uma viagem longa, o valor cobrado será: R${d*0.45:.2f}')