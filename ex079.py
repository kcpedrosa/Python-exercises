lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado. ACESS DENIED')
    perg = str(input('Quer continuar? [S/N]  ')).lower()
    if perg in 'n':
        break
print(f'Você digitou {sorted(lista)}')