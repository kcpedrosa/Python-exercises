#fiz uma lista jogando num dict MAS era pra fazer o oposto
lista = []
dados = {}
while True:
    lista.append(str(input('Digite o NOME da pessoa:  ')))
    while True:
        perg = str(input('Digite o SEXO da pessoa [Digite M/F]:  '))
        if perg not in 'FfMm':
            print('ERRO! Digite novamente o sexo')
        else:
            lista.append(perg)
            break
    lista.append(int(input('Digite a IDADE da pessoa:  ')))
    dados['Dados'] = lista[:]

    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break

print('=-'*30)
print(lista)
print(dados)



