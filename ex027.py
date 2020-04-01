n = str(input('Digite seu nome completo aqui: ')).strip()
nome = n.split()
#testando o split, pra deixar claro o q ele faz
print(nome)
#agora colocando posições
print(nome[0])
#agora escrevendo tudo bonito
print('Seu primeiro nome é {}.'.format(nome[0]))
#nao funciona colocar so nome[len(nome)] pq ele no caso de 'maria sa sao'
#dá 3 sendo que sao é 2, e o que queremos é o 2 [0,1,2]
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))