v = float(input('Qual valor da compra? R$'))
fp = int(input('[ 1 ] A vista dinheiro/cheque:\n[ 2 ] No debito:\n[ 3 ] 2x no credito:\n[ 4 ] 3x ou mais no credito:\nQual será a forma de pagamento? '))

if fp == 1:
    dc = v * 0.10
    print(f'A vista, sua compra terá um desconto de R${dc:.2f}')
    print(f'Sua compra de R${v:.2f}, vai custar R${v - dc:.2f}')
elif fp == 2:
    db = v * 0.05
    print(f'No débito, sua compra terá um desconto de R${db:.2f}')
    print(f'Sua compra de R${v:.2f}, vai custar R${v - db:.2f}')
elif fp == 3:
    print(f'Sua compra será parcelada em 2x no crédito sem juros')
    print(f'Sua compra de R${v:.2f}, vai custar R${v:.2f}')
elif fp == 4:
    tp = int(input('Em quantas vezes quer parcelar? '))
    cr = v * 0.20
    p = cr / tp
    print(f'Sua compra será parcelada em {tp}X com juros de R${p:.2f} por parcela.')
    print(f'Sua compra de R${v:.2f}, vai custar R${v + cr:.2f}')
else: 
    print('Forma de pagamento invalida, tente novamente.')