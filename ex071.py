print('=-' * 25)
print('{:^40}'.format('BANCO DEUTSCHES BANK'))
print('=-' * 25)
valor = int(input('Digite o valor a ser sacado: R$  '))
total = valor
totalced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        #if totalced > 0 de um tab no print abaixo, o programa nao vai printar nada se
        #o numero de cedulas for zero, ex 0 cedulas de $ 20
        print(f'Total de {totalced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=-' * 20)
print('SO LONG')