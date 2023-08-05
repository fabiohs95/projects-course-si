def classifica_numero(numero):
    if numero % 3 == 0  and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero
numero= int(input("Insira um número iteiro: "))
classe= classifica_numero(numero)
print(classe)