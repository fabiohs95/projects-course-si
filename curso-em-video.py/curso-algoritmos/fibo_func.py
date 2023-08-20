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
n= int(input('Digite um número: '))
print(f'A sequência de fibonacci com {n} números é:')
f= fibo(n)
print('='*50)
flag= str(input('Quer entrar com um novo valor? (S/N): ')).strip().lower()
while flag == 's':
    n=int(input('Insira um novo valor: '))
    f= fibo(n)
    flag= str(input('Quer entrar com um novo valor? (S/N): ')).strip().lower()
    breakpoint
    print('='*50)
if flag == 'n':
    print('Tá bom, então!\nAté mais!')
    print('='*50)