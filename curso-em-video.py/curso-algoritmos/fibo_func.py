def fibo (a):
    n1= 0
    n2= 1
    n3= 1
    for i in range(0, a):
        n3= n2 + n1
        n1= n2
        n2= n3
        print(n1)

print('='*50)
try:
    n= int(input('\033[1;30;42mDigite um número:\033[m '))
    print(f'\033[1;32m sequência de fibonacci com {n} números é:\033[m')
    f= fibo(n)
    print('='*50)
    flag= str(input('\033[1;34mQuer entrar com um novo valor? (S/N):\033[m ')).strip().lower()
    while flag == 's':
        n=int(input('\033[1;32mnsira um novo valor:\033[m '))
        f= fibo(n)
        flag= str(input('\033[1;34mQuer entrar com um novo valor? (S/N):\033[m ')).strip().lower()
        breakpoint
        print('='*50)
    if flag == 'n':
        print('\033[1;33mTá bom, então!\nAté mais\033[m')
        print('='*50)
except Exception as error:
    print('\033[1;41mEntrada inválida\033[m' )