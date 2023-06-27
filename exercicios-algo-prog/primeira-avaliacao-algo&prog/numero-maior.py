lista= []
for cont in range(0, 3):
    lista.append(float(input("digite um valor: ")))
print(f"dentre os números {lista} \n O maior é:>>{round(max(lista), 2)}<<")