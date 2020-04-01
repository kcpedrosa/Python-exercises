#esse programa vai calcular o IMC e definir categorias
massa = float(input('Digite a sua massa[peso] em kgs: '))
h = float(input('Digite a sua altura em metros: '))
imc = massa/(h * h)
print('Seu IMC é de {}'.format(imc))
if imc < 17:
    print('Você está MUITO ABAIXO DO PESO, atenção!')
elif imc >=17 and imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc>= 18.5 and imc <= 25:
    print('Você está no peso IDEAL')
elif imc > 25 and imc <= 30:
    print('Você está com SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Você está com OBESIDADE')
elif imc > 40:
    print('Você está com OBESIDADE MORBIDA')


