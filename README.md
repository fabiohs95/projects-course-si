# projects-course-si
 Este repositório foicriadopara fins de ompartilhamentos de códigos escritos durante o  proesso de aprendizado do curso de sistemaspara internet na UNCISAL

segue abaixo  alguns códgo  simples já testados mas que podem gerar algumas issues ocasionais. Por favor, não exite em mandar sua issue ou  pull request!

import random
num_aleatorio = random.randint(0,100)
a = int(input("digite un número entre 0 e 100"))
print ("resultado do sorteio: {}".format(num_aleatorio))
print("Parabéns!! se fosse a Mega-Sena você estaria milionário" if a == num_aleatorio else "Vixe, está sem sorte")
