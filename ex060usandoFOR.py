n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
for num in range(0,n):
    print('{}'.format(c))
    print('x', end=' ') if c > 1 else print('=', end=' ')
    f = f * c
    c = c - 1
print('O fatorial de {} é {}'.format(n, f))
