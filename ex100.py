#projetar função sorteia e somapar
def sorteia(lista):
    from random import randint
    from time import sleep
    print('Sorteando 5 numeros...')
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f' {n} ', end=' ')
        sleep(0.5)
    print(lista)
    print('FIM!')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A lista foi {lista}')
    print(f'A soma dos valores PARES foi {soma}')
    print('FIM!')


#O programa principal vai abaixo
lista=[]
sorteia(lista)
somapar(lista)