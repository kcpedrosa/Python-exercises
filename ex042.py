#classificar triangulos e mostrar tipos
print('Este programa analisa possíveis triangulos')
l1 = float(input('Digite o valor do lado 1: '))
l2 = float(input('Digite o valor do lado 2: '))
l3 = float(input('Digite o valor do lado 3: '))
if l1>(l2 + l3) or l2>(l1 + l3) or l3>(l1 + l2):
    print('Não é possível formar um triangulo')
else:
    print('É possível formar um triangulo')
    #voce pode escrever no fim da linha acima ,end=' ' e a linha abaixo cola na ultima linha
    if l1 == l2 == l3:
        print('Este triangulo é EQUILATERO')
    elif l1 != l2 != l3 != l1:
        #a igualdade pode ser inclusiva, mas a diferença NÃO
        print('Este triangulo é ESCALENO')
    else:
        print('Este triangulo é ISOSCELES')

