#um contador que vai e volta, atenção!
def contador(i, f, p):
    from time import sleep
    print(f'Contando de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            sleep(1)
            print(f' {cont} ', end=' ')
            cont += p
        print('THATS ALL FOLKS')
    elif i > f:
        cont = i
        while cont >= f:
            sleep(1)
            print(f' {cont} ', end=' ')
            cont -= p
        print('THATS ALL FOLKS')


#programa principl abaixo
contador(0,50,10)
contador(30,0,5)