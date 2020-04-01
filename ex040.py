#o programa dirá se o aluno foi reprovado etc a partir de sua média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A media do aluno foi {}'.format(media))
if media < 5:
    print('O aluno foi REPROVADO')
elif media >=5 and media < 7:
    #poderia ter escrito 7 > media >=5
    print('O aluno está em RECUPERAÇAO')
else:
    print('O aluno foi APROVADO')