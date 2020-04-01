temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite o NOME: ')))
    temp.append(float(input('Digite o PESO [em kgs]: ')))
    if len(princ)==0:
        mai = men = temp[1]
    else:
        if temp[1]>mai:
           mai = temp[1]
        if temp[1]<men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    perg = str(input('Quer continuar? [S/N]  '))
    if perg in 'Nn':
        break
print('=-'*30)
print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi o de {mai} KGs e pertence a ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[ {p[0]} ]', end='')
print(f'\nO menor peso foi o de {men} KGs e pertence a ', end='')
for p in princ:
    if p[1] == men:
        print(f'[ {p[0]} ]', end='')