lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor:  ')))
print('=-'*30)
print('Os valores pares foram', end='')
for pos, c in enumerate(sorted(lista)):
    if c % 2 ==0:
        print(f' {c} ', end='')

print(f'\n {lista}')