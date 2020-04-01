def teste(b):
    #cria um novo A com escopo local
    global a
    #esse comando acima indica que ele n criará um novo A, mas usará o A global, usando
    #o parametro abaixo [a = 8]
    a = 8
    b +=4
    c = 2
    print(f'O A dentro vale {a}')
    print(f'O B dentro vale {b}')
    print(f'O C dentro vale {c}')

#esse a tem escopo global
a = 5
teste(a)
print(f'A fora vale {a} ')
#esse comando abaixo dará erro pois C tem escopo local e foi definido apns na DEF
#print(f'C fora vale {c} ')