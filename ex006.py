n = int(input ('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print ("O dobro de {} vale {}, \n o triplo vale {} \n e a raiz quadrada vale {:.3f}".format (n , d, t, r ))
#testando outras coisas
n = int(input ('Digite um número: '))
d = n * 2
t = n * 3
r = pow (n, (1/2))
print ("O dobro de {} vale {}, \n o triplo vale {} \n e a raiz quadrada[POW] vale {:.3f}".format (n , d, t, r ))
