#Lista de Preços com Tupla
lista = ('Lápis', 1.20, 'Borracha', 2,
         'Caneta', 4, 'Caderno', 20, 'Estojo', 6)
print('=-'*25)
print(f'{"LISTA DE PREÇOS":^35}')
for pos in range (0, len(lista)):
    if pos % 2 ==0:
        print(f'{lista[pos]:.<30}', end='')
    elif pos % 2 ==1:
        print(f'R${lista[pos]:>8.2f}')
print('=-'*25)
