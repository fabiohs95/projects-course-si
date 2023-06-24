n1= float(input("digite o primeiro número: "))
n2= float(input("digite o segundo número: "))
n3= float(input("digite mais um número: "))
lista= []
lista.extend([n1, n2, n3])
print(f"dentre os números {lista} \n O maior é:>>{round(max(lista), 2)}<<")