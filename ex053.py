#esse é dificil, detectador de palindromos
#refletir sobre esse codigo
frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Voce digitou o seguinte: {} '.format(frase))
#apenas para ver a diferença
print('Voce digitou o seguinte: {} '.format(palavras))
print('Voce digitou o seguinte: {} '.format(junto))
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
        print('o que vc digitou é um palindromo')
else:
        print('o que vc digitou NAO e um palindromo')