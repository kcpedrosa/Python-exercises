fatorial = int(input('digite um número para calcular seu fatorial: '))
print(fatorial, end=' = ')
resultado = 1
for c in range(1, fatorial):
    print(c, end=' x ')
    resultado *= c
print(f'{c + 1} = {resultado * (c + 1)}')