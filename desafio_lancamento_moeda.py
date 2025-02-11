'''
💡 Desafio: Crie um programa que:

Solicite ao usuário:
    1) A quantidade de lançamentos de uma moeda (cara ou coroa).

Simule os lançamentos e exiba:
    1) A proporção de caras e coroas observadas.
    2) A probabilidade de obter cara ou coroa.

'''

import numpy as np

print('=*='*40)
print('\n                                        PROBABILIDADE E PROPORÇÃO          \n')
print('=*='*40)

while True:
    try:
        qtd_lancamento = int(input('\n\nDigite a quantidade de lançamentos de uma moeda: '))
        if qtd_lancamento > 0:
            break
        else:
            print('A quantidade de lançamentos precisa ser maior que zero!')
    except ValueError:
        print('\n** VALOR INCORRETO!! Por favor, insira número inteiro positivo.')


# Quantidade de lançamento de cada um (1 = Cara, 2 = Coroa)
lancamentos = np.random.randint(1, 3, qtd_lancamento)

# Calculando a frequência de cada valor
valores, contagens = np.unique(lancamentos, return_counts=True)

# Criando um dicionário para armazenar os dados corretamente
resultados = {1: "Cara", 2: "Coroa"}
contagem_resultados = {resultados[valores[i]]: contagens[i] for i in range(len(valores))}

# Calculando a probabilidade
probabilidade = {chave: (valor / qtd_lancamento) * 100 for chave, valor in contagem_resultados.items()}



print()
print('=*='*40)
print('\nResultados:\n')

for lado, vezes in contagem_resultados.items():
    print(f'- {lado}: {vezes} vezes')


print(f'\nProbabilidade teórica:')
for lado, prob in probabilidade.items():
    print(f'- {lado}: {prob:.2f}%')

print()
print('=*='*40)

