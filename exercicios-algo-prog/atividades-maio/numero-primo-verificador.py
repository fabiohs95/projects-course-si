def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    try:
        num = int(input("Digite um número inteiro e positivo: "))
        if num <= 0:
            raise ValueError
        if is_prime(num):
            print(f"O número {num} é primo.")
        else:
            print(f"O número {num} não é primo.")
    except ValueError:
        print("Erro: Digite um número inteiro e positivo válido.")

if __name__ == "__main__":
    main()
