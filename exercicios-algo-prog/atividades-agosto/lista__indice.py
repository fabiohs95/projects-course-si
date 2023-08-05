L = [15, 7, 27, 39]
p = int(input("Digite um valor: "))
x = 0
while x < len(L):
    if L[x] == p:
        break
    x += 1
if x  < len(L):
    print(p, x)
else:
    print(p)
#resposta letra (b)