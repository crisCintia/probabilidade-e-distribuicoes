# Probabilidade e Distribuições Estatísticas 🎲📊

Este repositório contém implementações de conceitos fundamentais de **Probabilidade e Estatística**, incluindo **simulação de lançamentos de moeda** e **geração de distribuições estatísticas**.

## 📌 Projetos Implementados

### 🎯 Simulação de Lançamento de Moeda
- O programa solicita ao usuário a quantidade de lançamentos.
- Simula lançamentos e calcula a proporção de "cara" e "coroa".
- Exibe a probabilidade observada e teórica.

### 🎯 Simulação de Distribuições Estatísticas
- O programa permite escolher entre **Distribuição Normal, Binomial ou Poisson**.
- Para Binomial, permite configurar **número de tentativas e probabilidade de sucesso**.
- Para Poisson, permite definir **média esperada de eventos (\(\lambda\))**.
- Gera gráficos para melhor visualização.

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/probabilidade-e-distribuicoes.git

2. Execute os scripts:
   - desafio_lancamento_moeda.py
   - distribuicoes_estatisticas.py

### 📌 Como instalar as dependências do requirements.txt?
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Tecnologias Utilizadas
- Python 3.13
- NumPy
- SciPy
- Matplotlib

## 🎯 Exemplo de saída - Lançamento de Moeda
1) Digite a quantidade de lançamentos: 10
   - Resultados:
      - Cara: 6 vezes
      - Coroa: 4 vezes
   - Probabilidade teórica:
      - Cara: 50.00%
      - Coroa: 50.00%

## 🎯 Exemplo de saída - Distribuições Estatísticas
1) Qual distribuição deseja visualizar (Normal, Binomial ou Poisson): Binomial
   - Qual o número de tentativas (n): 10
   - Qual a probabilidade de sucesso (0 a 1): 0.3

## 🚀 Melhorias Futuras
Aqui estão algumas melhorias planejadas para evolução do projeto:

1️⃣ Adicionar um menu de seleção numérico para escolher a distribuição.  
2️⃣ Permitir que o usuário defina média e desvio padrão na Distribuição Normal.   
3️⃣ Criar um dashboard interativo com `Streamlit`.   
4️⃣ Implementar testes automatizados usando `pytest`.  

## 🧑‍💻 Autor
- Desenvolvido por Cíntia Soares.

