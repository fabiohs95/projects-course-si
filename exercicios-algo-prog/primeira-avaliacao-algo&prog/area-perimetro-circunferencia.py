import math as m
raio= float(input("Digite o valor do raio da circunferência: "))
area= m.pi * m.pow(raio, 2)
peri= m.tau * raio
print("A área do circulo é: {:.2f}\nE seu perimetro é: {:.2f}".format(area, peri))
print("progama encerrado!")  