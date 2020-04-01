#fatorial
n = int(input('Digite um numero para saber seu FATORIAL: '))
c = n
f = 1
print( 'Calculando o FATORIAL de {} '.format(n))
while c > 0:
    print( ' {} '.format(c), end=' ')
    print (' x ', end=' ') if c > 1 else print('=', end=' ')
    f = f * c
    c = c - 1
print( 'O fatorial de {} é {}'.format(n,f))