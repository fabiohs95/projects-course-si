valor_total= int(input("Digite o valor total da compra:"))
if valor_total >= 100 and valor_total < 200:
    desc= 0.10 * valor_total
    print("O valor final da compra é R$ {}".format(valor_total - desc))
    print("Foi aplicado 10 % de desconto!")
elif valor_total >= 200 and valor_total < 500:
    desc= 0.20 * valor_total
    print("O valor final da compra é R$ {}".format(valor_total - desc))
    print("Foi apllcado 20 % de desconto!")
elif valor_total >= 500:
    desc= 0.30 * valor_total
    print("O valor final da compra é R$ {}".format(valor_total - desc))    
    print("Foi aplicado 30 % de desconto!")