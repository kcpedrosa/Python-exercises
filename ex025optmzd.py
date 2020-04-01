cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'fundociano': '\033[46m'}
n = str(input('Digite seu nome: ')).strip()
# O programa irá jogar tudo para minusculo.
n = n.lower()
n = str('silva' in n.split())
#Split will split a string into a list where each WORD is a list item:
#sendo assim ''Silvana Sá'' sera separada em silvana e sa
#e o programa nao vai dar falso positivo
if n == str('True'):
    print(f'Seu nome tem {cores["azul"]}Silva{cores["limpa"]}')
else:
    print(f'Seu nome não tem {cores["fundociano"]}Silva{cores["limpa"]}')