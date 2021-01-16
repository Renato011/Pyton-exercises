import math
ang = int(input('Me fale um ângulo que vou lhe mostrar o seno e coseno do mesmo.\nÂngulo: '))
rad = math.radians(ang)
coss = math.cos(rad)
seno = math.sin(rad)
print('O seno de {}° é {:.2f} e o coseno de {}° é {:.2f}.'.format(ang, seno, ang, coss))