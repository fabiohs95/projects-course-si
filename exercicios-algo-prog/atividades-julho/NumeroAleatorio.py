import random
menu= int(input("Escolha uma opção para definir o nível de dificuldade!\nOpção 1 (Fácil)\nOpção 2 (Médio)\nOpção 3 (Difícil)\nOpção 4 (Insano)\nDigite a opção:"))
if menu == 1:
    o1= int(input("Digite um número de 1 a 10:-> "))
    sort= random.randint(1, 10)
    cont= 1
    while o1 != sort:
        cont= cont + 1
        if o1 < sort:
            o1= int(input("Ainda não é esse!\nUm pouco mais pra  cima!\nDigite: "))
        elif o1 > sort:
            o1= int(input("Ainda não é esse!\nTente um pouco mais pra baixo!\nDigite: "))
    else:
        print("Parabéns! Você acertou na {}° tentativa! O número sorteado foi: {}".format(cont, sort))
