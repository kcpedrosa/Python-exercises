def funcmaior(*num):
    from time import sleep
    cont = maior = 0
    print('=-' * 30)
    print('Analisando numeros para retornar o MAIOR...')
    for c in num:
        sleep(0.5)
        print(f' {c} ')
        if cont == 0:
            maior = c
        elif c > maior:
            maior = c
        cont += 1
    sleep(0.5)
    print(f'O maior numero foi {maior}')


# programa principal
funcmaior(1, 3, 5)
funcmaior(2, -10, 5)
#até aqui está funcionando
lista = []
while True:
    perg = str(input('quer continuar? [S/N]:  '))
    if perg in 'Nn':
        break
    else:
        perg2 = int(input('Quantos numeros serao analisados? '))
        for c in range(0, perg2):
            perg3 = int(input('Digite o numero: '))
            lista.append(perg3)
        funcmaior(lista)
#PROBLEMA: A FUNÇAO INTERPRETOU A LISTA COMO UM NUMERO SÓ

