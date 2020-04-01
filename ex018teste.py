from math import radians, sin, cos, tan
ang = float(input('Digite o valor do angulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tang = tan(radians(ang))
print('Para o angulo {}, o valor do sin é {:.2f}, cos é {:.2f} e tan é {:.2f}'.format(ang,seno,cosseno,tang))
