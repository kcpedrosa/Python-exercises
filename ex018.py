#o seguinte programa usará funções mat.
import math
ang = float(input('Digite o valor do angulo: '))
cos = math.cos(math.radians(ang))
sin = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O valor do cos é {:.2f}, do sin é {:.2f} e da tg é {:.2f}'.format(cos,sin,tan))
