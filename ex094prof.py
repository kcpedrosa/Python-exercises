galera = []
lista = {}
soma = media = 0
while True:
    lista.clear()
    lista['Nome'] = str(input('Digite o NOME da pessoa:  '))
    while True:
        sexo = str(input('Digite o SEXO da pessoa [Digite M/F]:  ')).upper()[0]
        if sexo not in 'FfMm':
            print('ERRO! Digite novamente o sexo')
        else:
            lista['Sexo'] = sexo
            break
    lista['Idade'] = int(input('Digite a idade:  '))
    soma += lista['Idade']
    galera.append(lista.copy())
    while True:
        perg = str(input('Quer continuar? [S/N]  '))
        if perg not in 'NnSs':
            print('Erro! Digite novamente apenas S ou N')
        elif perg in 'NnSs':
            break
    if perg in 'Nn':
        break

print('=-'*30)
print(galera)
print('=-'*30)
print(f'A)  Ao todo foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'B)  A MÉDIA das idades foi {media:.2f} anos')
print('C) As mulheres cadastradas foram', end=' ')
for c in galera:
    if c['Sexo'] in 'Ff':
        print(f' [ {c["Nome"]} ] ', end=' ')
print()
print('D) A(s) pessoa(s) acima da MEDIA de IDADE foi/foram ', end=' ')
for c in galera:
    print()
    if c['Idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v} ', end='')
print()
print('FIM DO PROGRAMA')
