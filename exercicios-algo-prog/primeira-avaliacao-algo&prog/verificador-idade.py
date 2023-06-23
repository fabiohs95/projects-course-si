idade= int(input("Digite sua idade:"))
print("Verificando a faixa etária... Aguarde, por favor!")
if idade < 12:
    print("{} anos é considerado criança".format(idade))
elif idade > 12 and idade < 18:
    print("{} anos é cosiderado adolescete".format(idade))
elif idade > 17 and idade < 60: 
    print("{} anos é considerado adulto".format(idade))
elif idade > 59:
    print("{} anos é considerado idoso".format(idade))