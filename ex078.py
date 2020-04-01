#digite 5 numeros e o programa vai dizer quem é o maior E sua posição
lista=[]
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(f'Você digitou {lista}')
print(f'O maior valor foi {max(lista)} ...', end='')
for pos, c in enumerate(lista):
    if c == max(lista):
        print(f'na posição {pos}', end=' ')
print(f'\nO menor valor foi {min(lista)} ...', end='')
for pos, c in enumerate(lista):
    if c == min(lista):
        print(f'na posição {pos}', end=' ')
