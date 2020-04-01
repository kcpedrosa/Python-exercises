palavras=('aprender','mouse','teclado','monitor', 'grátis', 'purê')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for k in p:
        #quando digitamos 'k' no FOR... IN, criamos a variável
        if k.lower() in 'aeiouáéíóúâêîôûãõ':
            print(k, end=' ')