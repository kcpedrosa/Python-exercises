lista=[]
mai = men = 0
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
#o prof usou um segundo if, sera que da problema?
        elif lista[c] < men:
            men = lista[c]
print('=-'*20)
print(f'\nO maior valor foi {mai} ...', end='')
for pos, c in enumerate(lista):
    if c == mai:
        print(f'na posição {pos}', end=' ')
print(f'\nO menor valor foi {men} ...', end='')
for pos, c in enumerate(lista):
    if c == men:
        print(f'na posição {pos}', end=' ')
