num= int(input("Digite um número inteiro qualquer:"))
if num % 1 == 0 and num % num == 0 and num != 1:
  print("O número {} é primo!".format(num))
elif num % 1 != 0 and num % num != 0:
  print("O número {} não é primo!".format(num))