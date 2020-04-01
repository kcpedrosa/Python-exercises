#essa função é curiosa
def leiaInt(msg):
    '''
    --->Essa função analisa se o dado passado é um numero
    :param msg: um dado
    :return: valor
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número  ')
print(f'Você digitou o numero {n}')