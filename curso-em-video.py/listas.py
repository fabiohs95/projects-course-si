valores= []
for cont in range(0, 5):
    valores.append(int(input("digite um número; ")))
print(f"O maior número digitado foi: {round(max(valores))}\n O menor valor foi: {round(min(valores))}")