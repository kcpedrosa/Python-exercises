#classifica atletas pela antiguidade
from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} ano(s)'.format(idade))
if idade <= 9:
    print('Sua classificação é MIRIM')
elif idade > 9 and idade <=14:
    print('Sua classificação é INFANTIL')
elif idade > 14 and idade <=19:
    #na verdade n precisa do >14
    print('Sua classificação é JUNIOR')
elif idade > 19 and idade <=25:
    print('Sua classificação é SENIOR')
else:
    print('Sua classificação é MASTER')