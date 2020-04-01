#conversao de bases numericas[octal, binario etc]
numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão: \n[1] para BINARIO \n[2] para OCTAL \n[3] para HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print(' {} convertido para BINARIO é {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print(' {} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print(' {} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)))
else:
    print('Você está de sacanagem. Digite uma opção com valor de 1 a 3')
#o [2:]faz a leitura do digito na posição apos a 2 ate o fim
#0b é binario 0o é octal e 0x é hexadecimal, mas podemos cortar esse inicio