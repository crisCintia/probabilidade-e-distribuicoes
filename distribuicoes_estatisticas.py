'''
Desafio - Crie um programa que:

1️⃣ Pergunte ao usuário qual distribuição deseja visualizar (Normal, Binomial ou Poisson).
2️⃣ Gere e plote a distribuição escolhida.
3️⃣ Para a Distribuição Binomial, pergunte ao usuário o número de tentativas e a probabilidade de sucesso.
4️⃣ Para a Distribuição Poisson, pergunte o valor de λ (média de eventos esperados).

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson 


print('='*100)
print('\n                               DISTRIBUIÇÕES ESTATÍSTICAS\n')
print('='*100)


while True:
    distrib = input('Qual distribuição deseja visualizar (Normal, Binomial ou Poisson): ').strip().lower()
    if distrib not in ['normal', 'binomial','poisson']:
        print('Entrada Incorreta! Por favor, insira a Distribuição Desejada (Normal, Binomial ou Poisson).')
    else:
        break

if distrib == 'normal':
    # Gerando dados com média 0 e desvio padrão 1
    dados = np.random.normal(0, 1, 1000)

    # Criando o histograma
    plt.hist(dados, bins = 30, density=True, alpha = 0.6, color = 'b')

    # Criando a curva normal
    x = np.linspace(-3, 3, 100)
    plt.plot(x, norm.pdf(x, 0, 1), 'r', label = 'Distribuição Normal')

    plt.title('Distribuição Normal')
    plt.legend()
    plt.show()

elif distrib == 'binomial':
    while True:
        try:
            n = float(input('Qual o número de tentativas (n): '))
            p = float(input('Qual a probabilidade de sucesso (0 a 1): '))
            if 0 <= p <= 1 and n > 0:
                break
            else:
                print('Valores inválidos! O número de tentativas deve ser positivo e a probabilidade entre 0 e 1.')
        except ValueError:
            print('Erro! Insira números válidos para n e p.')

    x = np.arange(0, n+1)

    # Probabilidade de cada número de sucesso
    y = binom.pmf(x, n, p)

    # Criando a Distribuição Binomial
    plt.bar(x, y, color='c')
    plt.xlabel('Número de Sucessos')
    plt.ylabel('Probabilidade')
    plt.title('Distribuição Binomial')
    plt.show()

elif distrib == 'poisson':
    while True:
        try:
            valor_lambda = float(input('Qual o valor de Lambda (λ): '))
            if valor_lambda > 0:
                break
            else:
                print('O valor de Lambda deve ser positivo.')
        except ValueError:
            print('Erro! Insira um número válido para Lambda.')

    # Gerando a distribuição de poisson
    dados_poisson = poisson.rvs(mu = valor_lambda, size = 1000)

    # Criando o gráfico da distribuição
    plt.hist(dados_poisson, bins = 20, density=True, alpha = 0.7, color = 'g')
    plt.xlabel('Ocorrências')
    plt.ylabel('Frequência')
    plt.title('Distribuição de Poisson')
    plt.show()