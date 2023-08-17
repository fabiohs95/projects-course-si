from time import sleep
print('\033[1;30;42mSeja Bem-Vindo(a)!\033[m')
sleep(1)
print('\033[1mVamos começar:\033[m')
def ParOuImpar(x):
    if (x) % 2 == 0:
        print(f'o valor \033[7m {x} \033[m é \033[7m PAR \033[m')
    else:
        print(f'O valor \033[7m {x} \033[m é \033[7m IMPAR \033[m')
try:
    flag= 's'
    while flag == 's':
        n= int(input('\033[1;32mDigite um valor inteiro:\033[m '))
        print('\033[1;34maguarde um segundo...\033[m')
        sleep(1)
        r= str (ParOuImpar(n))
        flag= str(input('Quer continuar? (\033[1;32mS\033[m/\033[1;31mN\033[m): ')).strip().lower()
        breakpoint
    if flag == 'n':
        print('\033[1;34mProgama encerrado.\nAté mais!\033[m')
    else:
        while flag != 's' and flag != 'n':
            print('\033[1;33mdigite (S) para continuar ou (N) para encerrar o progama!\033[m')
            print('\033[1;33mO Progama foi encerrado!\033[m')
            break
except Exception as error:
    print('\033[1;30;41mEntrada iválida\033[m\n\033[1;31mDigite apenas números inteiros!\033[m')