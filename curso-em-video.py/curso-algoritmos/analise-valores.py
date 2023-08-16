from time import sleep
print('\033[1;35m('*10,'Bem-vindo(a)!',')'*10,'\033[m')
print('Digite 5 valores para começar')
soma=0
div5=0
null=0
SomaPar=0
for i in range(0, 5):
    v=int(input(f'\033[1;42mInsira o {i+1}° valor:\033[m '))
    soma= soma+v
    if v % 5 == 0:
        div5= div5 + 1
    if v == 0:
        null= null+1
    if v % 2 == 0:
        SomaPar= SomaPar+v
print('Analisando os valores...')
sleep(2)
print('='*50)
print(f'''\033[1;32mA soma entre esse valores é: {soma}
A média desses valores é igual à: {soma/5}
Números divisiveis por 5: {div5}
Quantidade de valores nulos: {null}
A soma dos números pares é: {SomaPar}\033[m''') 
print('='*50)