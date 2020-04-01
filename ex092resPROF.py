#essa resolução considera o TEMPO DE CONTR como parametro
from datetime import date
dados = {}
dados['Nome'] = str(input('Digite o nome:  '))
dados['Nascimento'] = int(input('Digite o ano de nascimento:  '))
dados['CTPS'] = int(input('Digite o número da CTPS [0 = não tem]: '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Digite o ano de contratação:  '))
    dados['Salário'] = float(input('Digite o salário em R$: '))
    idade = (date.today().year) - dados['Nascimento']
    dados['Aposentadoria'] = idade + ((dados['Ano de contratação']+35)-(date.today().year))

print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'  -   {k} tem o valor {v}')