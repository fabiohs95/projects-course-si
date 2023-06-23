sal_bruto= float(input("Digite seu salário bruto em R$:"))
if sal_bruto <= 1320:
    inss= (7.5/100) * sal_bruto
    sal_liqui= sal_bruto - inss
    print("seu salário liquido já descontanto INSS e IRPF é R4 {}".format(sal_liqui))
elif sal_bruto > 1320 and sal_bruto <= 2571.29:
    inss= (9/100) * sal_bruto    
    irpf= (7.5/100) * sal_bruto
    sal_liqui= sal_bruto - (inss + irpf)
    print("seu salário liquido já descontanto INSS e IRPF é R$ {}".format(sal_liqui) if sal_bruto >= 1903.99 and sal_bruto <= 2826.65 else " seu salário - inss é R$ {:.2f}".format(sal_bruto-inss) ) 
elif sal_bruto >= 2571.30 and sal_bruto <= 3856.94:
    inss= (12/100) * sal_bruto
    irpf= (15/100) * sal_bruto
    sal_liqui= sal_bruto - (inss + irpf)
    print("seu salário liquido já descontanto INSS e IRPF é R4 {}".format(sal_liqui) if sal_bruto >= 2826.66 and sal_bruto <= 3751.05 else "seu salário - inss é R${:.2f}".format(sal_bruto-inss))
elif sal_bruto >= 3856.95:
    inss= (14/100) * sal_bruto
    irpf= (22.5/100) * sal_bruto
    sal_liqui= sal_bruto - (inss + irpf)
    print("seu salário liquido já descontanto INSS e IRPF é R$ {}".format(sal_liqui))