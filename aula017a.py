lista=[]
lista.append(1)
lista.append(2)
lista.append(3)
print(lista)
lista=[]
for c in range(0,4):
    lista.append(int(input('Digite um valor: ')))

for c in lista:
    print(f' {c}...', end=' ')
for pos, c in enumerate(lista):
    print(f'\nNa posição {pos} encontrei o valor {c}...')

