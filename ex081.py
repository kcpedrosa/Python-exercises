lista = []
while True:
    lista.append(int(input('Digite um valor:  ')))
    perg = str(input('Quer continuar? [S/N]  '))
    if perg in 'Nn':
        break
print(lista)
print(f'Você digitou {len(lista)} elemento[s]')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
for pos, c in enumerate(lista):
    if c == 5:
        print(f'O valor 5 está na lista na posição {pos}')
if 5 not in lista:
    print('O valor 5 não está na lista')
