#essa resolução considera o TEMPO DE CONTRIB de 30 anos como parametro
from datetime import date
dados = {}
dados['Nome'] = str(input('Digite o nome:  '))
dados['Nascimento'] = int(input('Digite o ano de nascimento:  '))
dados['CTPS'] = int(input('Digite o número da CTPS [0 = não tem]: '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Digite o ano de contratação:  '))
    dados['Salário'] = float(input('Digite o salário em R$: '))
    tempotrabalhando = (date.today().year) - dados['Ano de contratação']
    tempocontribuiçãofaltando = 30 - tempotrabalhando
    idade = (date.today().year) - dados['Nascimento']
    anoaposentadoria = (date.today().year) + tempocontribuiçãofaltando
print('=-'*30)
print(f'{dados["Nome"]} contribuiu por {(date.today().year) - dados["Ano de contratação"]}')
print('=-'*30)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')
print(f'{dados["Nome"]} se aposentá daqui a {tempocontribuiçãofaltando} anos'
      f' Exatamente no ano de {anoaposentadoria}')
