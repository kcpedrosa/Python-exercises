frase = str(input('Digite uma frase aqui: ')).strip()
frase = frase.lower()
letra = str(input('Digite uma letra: '))
letra = letra.lower()
print('A letra {} aparece {} vez(es) na frase'.format(letra, frase.count(letra.lower())))
#preciso alterar essa parte de baixo pra funcionar com qualquer letra
#perguntar pra alguem como resolver isso
print('A primeira letra {} apareceu na posição {}'.format(letra, frase.find('a')+1))
print('A primeira letra {} apareceu na posição {}'.format(letra, frase.rfind('a')+1))