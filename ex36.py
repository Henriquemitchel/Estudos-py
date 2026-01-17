print('=='*20)
print('SIMULE SEU EMPRESTIMO!')
print('==' *20)
vc = float(input('Qual valor da casa? '))
s = float(input('Qual se salario? '))
a = int(input('Em quantos anos quer divir? ')) * 12
vm = vc / a
pm = s * 0.30
if vm > pm:
    print(f'\033[0;31mSEU EMPRESTIMO FOI NEGADO\033[m\nA parcela mensal de R${vm:.2f} ultrapassa a margem de 30% do seu salario.')
else:
    print(f'\033[0;32mPARABENS! SEU EMPRESTIMO FOI APROVADO\033[m\nA parcela mensal de R${vm:.2f} esta dentro da margem de 30% do seu salario.')
