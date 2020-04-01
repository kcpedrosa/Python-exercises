a = [2,3,4,5]
b = a
b[1]=8
#B na posição 1 recebe 8, veja que há reflexos em A também
print(f'Lista A : {a}')
print(f'Lista B : {b}')
a = [2,3,4,5]
b = a[:]
#aqui B vira uma copia de A, e a alteração posterior só afeta B
b[1]=8
print(f'Lista A : {a}')
print(f'Lista B : {b}')
#ultimo teste
x = [8,8,13,27,0]
print(sorted(x))
print(sorted(x, reverse=True))
print(f'Essa lista tem {len(x)} elementos')
x.remove(8)
#removerá apenas o primeiro '8', mas fazendo um FOR dá pra remover todos os '8'
print(x)
for c in x:
    if c == 8:
        x.remove(8)
print(x)
