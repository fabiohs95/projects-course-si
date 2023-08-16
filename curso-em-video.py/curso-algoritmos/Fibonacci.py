from time import sleep
try:
    print('\033[1;32mBem-vindo!\033[m\n\033[1;;42mGerador de Fibonacci.py\033[m')
    qtd= int(input('\033[7mDigite a quantidade de números para a sequência:\033[m '))
    ante= 0
    prox= 1
    soma= 1
    print("Aguarde um sengundo...")
    sleep(2)
    print('-'*50)
    for i in range(0, qtd):
        soma= prox + ante
        ante= prox
        prox= soma
        print(f'Posição:\033[1;32m{i+1}\033[m \033[1;38mé igual à: {ante}\033[m')
    print('-'*50)
except Exception as error:
    print('\033[1;31mErro!\nInsira apenas números inteiros!\033[m')