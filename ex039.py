#o programa vai calcular se a pessoa vai se alistar[alist.militar]
from datetime import date
atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
genero = str(input('Digite seu gênero [M ou F)]: ')).upper().strip()
if genero == 'F':
    print('Você não precisa se alistar')
else:
    print('Você deve se alistar, porém veja instruções abaixo')
    idade = atual - ano
    print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, atual))
    if idade < 18 and ano < atual:
        print('Ainda faltam {} ano(s) para o seu alistamento'.format(18 - idade))
        print('Seu alistamento será em {}'.format(ano + 18))
    elif idade > 18:
        print('Você deveria ter se alistado há {} ano(s)'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(ano + 18))
    elif idade == 18:
        print('Vá se alistar IMEDIATAMENTE')
    elif ano > atual:
        print('LOGO, VOCÊ VEIO DO FUTURO!!!')
        print('Ainda faltam {} ano(s) para o seu alistamento'.format(18 - idade))
        print('Seu alistamento será em {}'.format(ano + 18))

