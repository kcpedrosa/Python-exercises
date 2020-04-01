print('=-' * 20)
print('{:^30}'.format('DEUTSCHES BANK'))
print('=-' * 20)
valor = int(input('Digite o valor que deseja sacar: R$ '))
total = valor
ced = 50
totalced = 0
#troquei total por valor na prox linha por isso o problema
while True:
    if total >= ced:
        valor -= ced
        totalced += 1
    else:
        print('Foram sacadas {} cedulas de R$ {}'.format(totalced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Adeus, volte sempre')
