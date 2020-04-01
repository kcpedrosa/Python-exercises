#condição de existencia de triangulos
print('Esse programa vai analisar se é possivel formar um triangulo de acordo coma medida do lado')
print('-=-'*20)
l1 = float(input('Digite a medida do lado 1: '))
l2 = float(input('Digite a medida do lado 2: '))
l3 = float(input('Digite a medida do lado 3: '))
if l1>(l2 + l3) or l2>(l1+l3) or l3>(l1+l2):
    print('NÃO pode ser um triangulo')
else:
    print('É triângulo')
