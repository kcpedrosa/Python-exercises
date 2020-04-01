#validação uso de dados e uso do WHILE
sexo = str(input('Digite o sexo: ')).strip().upper()
while sexo not in  ['M', 'F', 'HOMEM', 'MULHER', 'MASCULINO', 'FEMININO']:
    sexo = str(input('Dados invalidos. Digite o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))