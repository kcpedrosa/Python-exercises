lista =[]
listpar = []
listimpar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listpar.append(num)
    else:
        listimpar.append(num)
    perg = str(input('Quer continuar? [S/N]  '))
    if perg in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'Os numeros pares foram {listpar} e os impares {listimpar}')