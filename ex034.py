#calculador de aumentos em salários
salario = float(input('Digite o valor do seu salário: '))
if salario > 1250.00:
    m1=salario*1.1
    print('Seu salário agora é de R$ {}'.format(m1))
else:
    m2=salario*1.15
    print('Seu salário agora é de R$ {}'.format(m2))

