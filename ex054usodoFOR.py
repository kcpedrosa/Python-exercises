#analise de dados: datas de nascimento, determinar quem é maior de idade
#voce pode digitar import datetime mas antes de cada operação que envolva essa biblioteca tens que
#digitar datetime. antes
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
#coloque o int input dentro do laço!!!
for pess in range(1,5):
    nasc = int(input('Em que ano a {} ª pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    print('A pessoa tem {} anos'.format(idade))
    if idade >=18:
        totmaior = totmaior + 1
        #print('Essa pessoa é maior')
    else:
        totmenor = totmenor + 1
        #print('Essa pessoa é menor')
print('Tivemos {} pessoa[s] maiore[s] e {} pessoa[s] menore[s]'.format(totmaior, totmenor))
