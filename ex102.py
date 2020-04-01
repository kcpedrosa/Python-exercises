#calculo de fatorial
def fatorial(num, show = False):
    '''--> Função para calcular o FATORIAL de um número
    num : insira um numero para calcular seu FATORIAL
    show = False : [param. opcional] insira  True para ver o cálculo
    return : retorna o FATORIAL de num
    '''
    f = 1
    for c in range(num, 0, -1):
        f = f * c
        if show == True:
            if c > 1:
                print(f'{c} X ', end='')
            else:
                print(f'{c} = ', end='')
    print( f'{f}' )
    print('FIM')


#main program
fatorial(3, show=True)
fatorial(9, show=True)

help(fatorial)
