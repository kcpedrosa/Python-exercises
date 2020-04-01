#tabuada usando while e for com o BREAK
while True:
    num = int(input('Digite um numero para ver sua tabuada: '))
    print('=-'*20)
    if num < 0:
        print('Nao faremos tabuada de num NEGATIVO nesse programa')
        break
    for c in range(1,11):
        print(f'{num} X {c} = {num * c}')

print('FIM da tabuada')