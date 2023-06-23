salario= int(input("Digite o valor do seu salário mensal em R$;"))
print("informação salva!")
emprestimo= int(input("agora digite o valor do empréstimo desejado:"))
print("informação salva!")
idade= int(input("Por fim, digite sua idade:"))
print("informação salva!")
print("Analisando os dados, só um segundo...")
if salario >= 2000 and emprestimo <= (10 * salario) and idade >= 18 and idade <=65:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo reprovado.")