print('Digite 5 valores para começar')
soma=0
div5=0
null=0
SomaPar=0
for i in range(0, 5):
    v=int(input(f'Insira o {i+1}° valor: '))
    soma= soma+v
    if v % 5 == 0:
        div5= div5 + 1
    if v == 0:
        null= null+1
    if v % 2 == 0:
        SomaPar= SomaPar+v
print(f'''A soma entre esse valores é: {soma}
A média desses valores é igual à: {soma/5}
Divisivel por 5 == {div5}
Valores nulos == {null}
A soma dos números pares é: {SomaPar}''') 