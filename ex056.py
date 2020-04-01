somaidade = 0
media = 0
maioridhom = 0
nomevelho = ''
totmulher20 = 0
for pess in range(1,3):
    print('--- {} ª pessoa ---'.format(pess))
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite  o sexo [M/F]:  ')).strip()
    somaidade = somaidade + idade
    if sexo in 'Mm' and pess == 1:
        maioridhom = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridhom:
        maioridhom = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
#copiado e colado porem nao entendido...
media = somaidade/2
print('A media das idades analisadas é: {:.2f} '.format(media))
print('O homem mais velho tem {} anos '.format(maioridhom))
print('O homem mais velho se chama {}'.format(nomevelho))
print('Nesse grupo há {} mulher[es] com menos de 20 anos'.format(totmulher20))