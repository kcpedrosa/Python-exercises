num=0
cont=0
soma=0
while num !=999:
    num=int(input('Digite um numero [digite 999 para parar]:'))
    cont=cont+1
    soma=soma+num
print('ACABOU')
print('Vc digitou {} numero[s] e a soma deles foi {}'.format(cont-1, soma-999))