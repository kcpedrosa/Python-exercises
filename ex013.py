salario = float(input('Digite o montante do salário: R$ '))
aumento = float(input('Digite o valor percentual do aumento: '))
salarionovo = salario * (1 + (aumento/100))
print ('Um funcionário que ganhava R$ {:.2f} , \ncom aumento de {} %, passa a receber R${:.2f}'.format(salario, aumento, salarionovo))