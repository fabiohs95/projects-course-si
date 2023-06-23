from datetime import date
#aqui estou definindo a idade mínima para jogar.
idade_min= 18
#agora vou solicitar as informações separadamente ao jogador.
ano= int(input("digite o ano de nascimento com 4 digitos:"))
mes= int(input("digite o mês de nasiento com 2 digitos (ex: 08):"))
dia=  int(input("digite o dia de nascimento com 2 digitos também:"))
print("Analisando  os dados! Aguarde...")
#agora vou usar a  biblioteca 'datetime' para obter a data atual.
data_atual= date.today()
#agora será feito o calculo da idade do jogador
idade= data_atual.year - ano
#agora será feita a verificação p/ saber se o jogador é elegível
if data_atual.month <= mes and data_atual.day >= dia and idade >= idade_min:
    print("Você pode jogar ojogo!")
else:
    print("Você não é elegível para jogar o jogo!")