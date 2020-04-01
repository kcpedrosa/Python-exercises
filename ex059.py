#Criando um Menu de Opções
from time import sleep
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
option = 0
while option != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do pragrama''')
    option = int(input('Digite a opção de acordo com o numero: '))
    if option == 1:
        print('O valor de {} + {} é {}'.format(n1, n2, n1+n2))
    elif option == 2:
        print('O valor de {} X {} é {}'.format(n1, n2, n1*n2))
    elif option == 3:
        if n1 > n2:
            print('O maior entre os dois é {}'.format(n1))
        else:
            print('O maior entre os dois é {}'.format(n2))
    elif option == 4:
        print('Digite novos números')
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
    elif option == 5:
        sleep(2)
        print('=-=' * 20)
        sleep(1)
        print('Fim do programa')
    else:
        print('Opção inválida. Digite uma opção válida')