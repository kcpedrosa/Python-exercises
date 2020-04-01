##066 - Vários números com flag, interrupção de WHILE com BREAK
num = 0
cont = soma = 0
while True:
    num = int(input('Digite um numero [e 999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('Voce digitou {} numero[s] e sua soma foi {}'.format(cont, soma))
