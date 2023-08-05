try:
    a=float(input("Insira o primeiro número: "))
    b=float(input("Insira o segundo número; "))
    o=input("escolha uma operação:\nDigite:\n(*,+,- ou /): ")

    if o == "+":
        resultado= a + b
    elif o == "-":
        resultado= a - b
    elif o == "*":
        resultado= a * b
    elif o == "/":
        resultado= a / b
    else:
        resultado= "operação inválida.\nvalor: 0"

    print(resultado)
except Exception as error:
    print("Executou a exception")