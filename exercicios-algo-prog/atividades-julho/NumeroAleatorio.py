import random
menu= int(input("Escolha uma opção para definir o nível de dificuldade!\nOpção 1 (Fácil)\nOpção 2 (Médio)\nOpção 3 (Difícil)\nOpção 4 (Insano)\nDigite a opção: "))
if menu == 1:
    n= int(input("Digite um número de 1 a 10:-> "))
    sorte= random.randint(1, 10)
    cont= 1
    while n != sorte:
        cont= cont + 1
        if n < sorte and sorte - n <= 2:
            n= int(input("Opa, quase!\nUm pouco mais pra  cima!\nDigite: "))
        elif n < sorte and sorte - n >= 3 and sorte - n < 6:
            n= int(input("Ainda não é esse!\nTente mais pra cima!\nO número está entre {} e {}\nDigite: ".format(n, sorte + 1)))
        elif n < sorte and sorte - n >= 6:
            n= int(input("Ainda não é esse!\nBem mais pra cima!\nDigite: "))
        elif n > sorte and n - sorte <=2:
            n= int(input("Opa, quase lá!\nTente um pouco mais pra baixo!\nO número está entre {} e {}\nDigite: ".format(n, sorte - 1)))
        elif n > sorte and n - sorte >= 3 and n - sorte < 6:
            n= int(input("Ainda não é esse!\nTente mais pra baixo!\nDigite: "))
        elif n > sorte and n - sorte >= 6:
            n= int(input("Ainda não é esse!\nBem mais pra baixo!\nDigite: "))
    else:
        print("Parabéns! Você acertou na {}° tentativa!\nO número sorteado foi: {}".format(cont, sorte))
if menu == 2:
    n= int(input("Digite um número de 1 a 50:-> "))
    sorte= random.randint(1, 50)
    cont= 1
    while n != sorte:
        cont= cont + 1
        if n < sorte and sorte - n <= 5:
            n= int(input("Ainda não é esse!\nUm pouco mais pra  cima!\nDigite: "))
        elif n < sorte and sorte - n >= 6 and sorte - n < 20:
            n= int(input("Ainda não é esse!\nTente mais pra cima!\nDigite: "))
        elif n < sorte and sorte - n >= 20:
            n= int(input("Ainda não é esse!\nBem mais pra cima!\nDigite: "))
        elif n > sorte and n - sorte <= 5:
            n= int(input("Ainda não é esse!\nTente um pouco mais pra baixo!\nDigite: "))
        elif n > sorte and n - sorte >= 6 and n - sorte < 20:
            n= int(input("Ainda não é esse!\nTente mais pra baixo!\nDigite: "))
        elif n > sorte and n - sorte >= 20:
            n= int(input("Ainda não é esse!\nBem mais pra baixo!\nDigite: "))
        while cont >= 5:
            print("Dica: Tente ir divindo pela metade! Ex: 50/2: 25...")
            break
    else:
        print("Parabéns! Você acertou na {}° tentativa!\nO número sorteado foi: {}".format(cont, sorte))