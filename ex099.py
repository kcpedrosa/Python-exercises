#programa para mostrar o maior
def funcmaior(* num):
    cont = 0
    maior = 0
    print('=-'*30)
    print('Analisando números para retornar o MAIOR...')
    from time import sleep
    for c in num:
        sleep(0.5)
        print(f' {c} ', end=' ')
        if cont == 0:
            maior = c
        elif c > maior:
            maior = c
        cont += 1
    sleep(0.5)
    print(f'\nO maior foi {maior}')


#programa principal
funcmaior(1,3,5)
funcmaior()
funcmaior(9,9,1,3)
funcmaior(10,14,-5,-20)

