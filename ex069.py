##069 - Análise de dados do grupo
print('=-'*20)
print('CADASTRE UMA PESSOA')
print('=-'*20)
conth=0
mais18 = 0
mulhermenos20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    if idade > 18:
        mais18 += 1
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    if sexo in 'Mm':
        conth += 1
    if sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print('O total de homens cadastrados foi de {}'.format(conth))
print(f'O total de pessoas com mais de 18 anos foi {mais18}')
print(f'Temos {mulhermenos20} mulher[es] com menos de 20 anos')