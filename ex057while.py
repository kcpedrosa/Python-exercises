#validação uso de dados e uso do WHILE
sexo = str(input('Digite o sexo: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos. Digite o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))