#programa pra identificaar se o ano é bissexto
from datetime import date
ano = int(input('Digite um ano, digite zero para o ano atual: '))
if ano == 0:
    ano = date.today().year
#se ano div por 4, nao divisivel por 100 exceto os div por 400, é bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} NAO é bissexto'.format(ano))
#Dados dois valores booleanos a e b, o operador lógico OR resulta em False
#apenas quando a e b foram ambos False, e retorna True em caso contrário.