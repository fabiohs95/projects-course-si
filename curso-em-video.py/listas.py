r= "S"
while not r:
    e= int(input("digite um número; "))
    r= str(input("Deseja continuar? [S/N]")).upper()
    if "S" < 2:
        print("O seu número da sorte é: {}".format(e))
    elif "S" > 2:
        print("Seu número da sote é a soma entre esses números {}".format(e))