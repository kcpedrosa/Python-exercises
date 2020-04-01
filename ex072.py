#mostrar numeros por extenso
cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número para ve-lo por extenso:  '))
    if 0 < num <=10:
        break
    print('Tente novamente')
print(f'O número é {cont[num]}')
while True:
    resp = str(input('Quer continuar [S/N] ?: ')).strip().upper()
    if resp in 'N':
        break
    else:
        num = int(input('Digite um número para ve-lo por extenso:  '))
        if 0 < num <= 10:
            print(f'O número é {cont[num]}')
print('Volte sempre')