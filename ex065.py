from statistics import mean
resp = 'S'
cont=0
lst=[]
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer continuar [S/N]?  ')).upper().strip()[0]
    cont = cont + 1
    lst += [num]
print('Você digitou {} números e a média deles é {}'.format(cont, mean(lst)))
print('O maior dentre os numeros que vc digitou é {} e o menor é {}'.format(max(lst),min(lst)))
print('ACABOU')