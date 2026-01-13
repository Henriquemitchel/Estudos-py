cid = str(input('Digite o nome da sua cidade: ')).strip()
cid = cid[:5].lower() == 'santo'
# cid = 'santo' in cid [:5]
print(f'Sua cidade começa com o nome Santo? {cid}')
