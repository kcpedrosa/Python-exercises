resp = 'S'
quant=0
#na pratica o prof chamou o contador de QUANT[substituiu]
media=0
soma=0
menor=maior=0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer continuar [S/N]?  ')).upper().strip()[0]
    quant = quant + 1
    soma = soma + num
    if quant == 1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        elif num<menor:
            num=menor
print('Você digitou {} números e a média deles é {}'.format(quant, soma/quant))
print('O maior dentre os numeros que vc digitou é {} e o menor é {}'.format(maior,menor))
print('ACABOU')