tabuada = int(input('Digite o numero da tabuada: '))
n = int(input('Digite o inicio da tabuada: '))
print ("Tabuada de %d" %tabuada)
if n <= 10:
        while n <= 10:
                print ("%d x %d =  %d" %(tabuada, n, tabuada * n))
                n = n + 1
else : print ('Você está de brincadeira. Digite um numero menor ou igual a 10')