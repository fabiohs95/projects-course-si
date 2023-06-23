from math import pow
metro= int(input("Digite um número em M (metros): "))
conv= int(input("escolha uma opção para converter: \n digite 1 para KM \n digite 2 para hm \n digite 3 para dam \n digite 4 para dm \n digite 5 para cm \n Ou 6 para mm >>>"))
km= metro * pow(10,-3)
hm= metro * pow(10,-2)
dam= metro * pow(10,-1)
dm= metro * 10
cm= metro * 100
mm= metro * 1000
if conv == 1:
    print("{} metros equivalem a {} km".format(metro, km))
elif conv == 2:
    print("{} metros equivalem a {} hm".format(metro, hm))
elif conv == 3:
    print("{} metros equivalem a {} dam".format(metro, dam))
elif conv == 4:
    print("{} metros equivalem a {} dm".format(metro, dm))
elif conv == 5:
    print("{} metros equivalem a {} cm".format(metro, cm))
elif conv == 6:
    print("{} metros equivalem a {} mm".format(metro, mm))
else:
    print("Opção inválida! Tente novamnete!")