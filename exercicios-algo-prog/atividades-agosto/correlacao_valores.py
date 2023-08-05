a=int(input("Digite um valor: "))
b=int(input("Digite outro valor: "))
c=int(input("Digite mais um valor: "))
m= a
if b > a and b > c:
    m = b
if c > a and c > b:
    m = c
mn= a
if b < a and b < c:
    mn= b
if c < a and c < b:
    mn= c
print(f"nesse caso *m* vale: {m}")
print(f"nesse caso *mn* vale: {mn}")
#resposta letra (b)