listapeso = []
listanome = []
while True:
    listanome.append(str(input('Digite o nome da pessoa: ')))
    listapeso.append(float(input('Digite o peso da pessoa em KGs:' )))
    perg = str(input('Quer continuar? [S/N]  '))
    if perg in 'Nn':
        break
print(listapeso, listanome)
print(f'O maior peso foi {max(listapeso)} e pertence a ')
print(f'{list.index(max(listapeso))}')

for pospeso, c in enumerate(listapeso):
    print(f'Na posição {pospeso} encontrei o valor {c}')