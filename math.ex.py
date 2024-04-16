from math import trunc, sin, radians, cos, tan

# quebrando um número
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hipo = (cato ** 2 + cata ** 2) ** (1/2)
print('A hipotenusa do triângulo vai medir {:.2f}'.format(hipo))

ang = int(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))