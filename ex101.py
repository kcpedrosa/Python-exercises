def voto(ano):
    from datetime import date
    print(f'O ano que você nasceu foi {ano}')
    idade = date.today().year - ano
    print(f'Você tem {idade} anos. Sua situação eleitoral é: ')
    if idade < 16:
        print(f'NÃO PODE VOTAR')
    elif 16 <= idade < 18 or idade > 70:
        print(f'VOTO FACULTATITO')
    else:
        print(f'VOTO OBRIGATÓRIO')


#eu usei print e o prof usou return [RETURN NAO FUNCIONOU]
#programa principal vai abaixo
voto(1946)
nasc = int(input('Em que ano você nasceu?  '))
voto(nasc)