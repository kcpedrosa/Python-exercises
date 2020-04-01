lista = [[] , []]
valor = 0
for c in range(1, 6):
    valor = int(input(f'Digite o {c}º valor:  '))
    if valor % 2 ==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('=-'*30)
print(f'Os valores digitados foram {lista}')
print(f'Os PARES EM ORDEM foram {sorted(lista[0])}')
print(f'Os IMPARES EM ORDEM foram {sorted(lista[1])}')