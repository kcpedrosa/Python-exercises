somaidade = 0
media = 0
maioridhom = 0
nomevelho = ''
nome = ''
list = []
listsexo = []
for pess in range(1, 3):
    print('--- {} ª pessoa ---'.format(pess))
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    list.append(idade)
    sexo = str(input('Digite  o sexo [M/F]:  ')).strip()
    listsexo.append(sexo)
    if sexo in 'Mn' and idade == max(list):
        nomevelho = nome
    somaidade = somaidade + idade
media = somaidade/2
print(list)
print(listsexo)
print('A media das idades analisadas é: {:.2f} '.format(media))
print('O homem mais velho tem {} anos '.format(max(list)))
print('O homem mais velho se chama {}'.format(nomevelho))
