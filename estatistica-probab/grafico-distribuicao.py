import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da distribuição normal
mu = 0   # Média
sigma = 1   # Desvio padrão

# Gere dados seguindo uma distribuição normal
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)   # Valores de x
y = norm.pdf(x, mu, sigma)   # Valores de y (probabilidade)

# Crie o gráfico
plt.plot(x, y, color='blue')
plt.title('Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.axvline(mu, color='r', linestyle='dashed', linewidth=1, label='Média')
plt.axvline(mu + sigma, color='g', linestyle='dashed', linewidth=1, label='Média + Desvio Padrão')
plt.axvline(mu - sigma, color='g', linestyle='dashed', linewidth=1, label='Média - Desvio Padrão')
plt.legend()
plt.grid(True)
plt.show()
