# 📈 Aula 9: Regressão Linear - Prevendo o Futuro com Matemática

## ⏱️ Cronograma da Aula (50 min)
* **(10 min) Introdução:** O que é regressão linear e suas aplicações
* **(15 min) Teoria:** Como funciona a "linha mágica" de previsão
* **(20 min) Prática:** Código em Python e visualização
* **(5 min) Desafio:** Exercício prático em duplas
* **Exemplo código:** https://colab.research.google.com/drive/1--FQRobNwoacAo1YBCuOnvcSBbRUqNI0?usp=sharing

## 🎯 Objetivo da Aula
Entender como a regressão linear permite prever valores numéricos a partir de dados existentes.

## 🧠 Conceito Simplificado
Regressão linear é como traçar a "melhor linha" através de pontos em um gráfico para descobrir a relação entre duas coisas e fazer previsões.

## 🚗 Analogia do Dia a Dia
**"Regra da Gasolina"**: 
- Imagine que você anota quanto seu carro anda (km) e quanto gasta de gasolina (R$)
- 100 km → R$ 50
- 200 km → R$ 100
- 300 km → R$ 150
- A regressão linear encontra essa relação (a cada 100 km, gasto R$ 50)
- Agora você pode prever: para andar 250 km, precisará de R$ 125

## 📊 Aplicações no Mundo Real
- Prever preços de imóveis com base no tamanho
- Estimar notas a partir de horas de estudo
- Prever vendas com base em gastos de publicidade
- Analisar relação entre saneamento e saúde pública

## 💻 Vamos Praticar no Colab!

```python
# Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# DADOS: Horas de estudo e Notas
horas_estudo = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)  # Precisa ser 2D
notas = np.array([50, 55, 65, 70, 75, 78, 85, 88])

# VISUALIZAR OS DADOS ORIGINAIS
plt.figure(figsize=(10, 6))
plt.scatter(horas_estudo, notas, color='blue', s=100)
plt.title('Relação entre Horas de Estudo e Notas', fontsize=16)
plt.xlabel('Horas de Estudo por Semana', fontsize=14)
plt.ylabel('Nota Final (0-100)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# CRIAR E TREINAR O MODELO
modelo = LinearRegression()
modelo.fit(horas_estudo, notas)  # O modelo "aprende" a relação

# VERIFICAR OS RESULTADOS
m = modelo.coef_[0]  # Coeficiente (inclinação da reta)
b = modelo.intercept_  # Intercepto (onde a reta cruza o eixo y)

print(f"Equação da reta: Nota = {m:.2f} × (Horas de Estudo) + {b:.2f}")
print(f"Interpretação: A cada hora extra de estudo, a nota aumenta {m:.2f} pontos")
print(f"Se não estudar nada (0 horas), a nota seria {b:.2f}")

# FAZER PREVISÕES
horas_para_prever = np.array([[6.5]])  # Exemplo: 6.5 horas
nota_prevista = modelo.predict(horas_para_prever)
print(f"\nSe um aluno estudar {horas_para_prever[0][0]} horas, sua nota será aproximadamente {nota_prevista[0]:.1f}")

# VISUALIZAR A LINHA DE REGRESSÃO
plt.figure(figsize=(10, 6))
plt.scatter(horas_estudo, notas, color='blue', s=100, label='Dados Reais')
plt.plot(horas_estudo, modelo.predict(horas_estudo), color='red', linewidth=3, label='Linha de Regressão')

# Destacar a previsão
plt.scatter(horas_para_prever, nota_prevista, color='green', s=150, marker='*', label='Previsão')

plt.title('Regressão Linear: Horas de Estudo vs. Notas', fontsize=16)
plt.xlabel('Horas de Estudo por Semana', fontsize=14)
plt.ylabel('Nota Final (0-100)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
```

## 🧩 Como Funciona por Trás dos Panos
A equação da reta é: **y = mx + b**

Onde:
- y é o valor que queremos prever (nota)
- x é o valor que conhecemos (horas de estudo)
- m é a inclinação (quanto a nota aumenta por hora de estudo)
- b é o intercepto (nota base sem estudo)

O algoritmo encontra os valores de m e b que melhor se ajustam aos dados.

## 📝 Exercício Prático
1. Modifique o código para prever o preço de casas com base em:
   - Tamanho (m²): [50, 65, 80, 95, 110, 125]
   - Preço (R$ mil): [150, 175, 210, 240, 270, 300]

2. Responda:
   - Qual seria o preço estimado de uma casa de 100m²?
   - Se a metragem aumentar em 10m², quanto o preço tende a aumentar?
   - O que significam o coeficiente e o intercepto neste contexto?

## 💡 Dicas para Bons Resultados
1. Verifique se existe uma relação linear entre suas variáveis
2. Remova outliers (valores muito fora do padrão)
3. Quanto mais dados, melhor a previsão
4. Cuidado com extrapolações muito distantes dos dados originais

## 🎯 Aplicação no Projeto Final
Exemplos de uso da regressão linear em seus projetos:
- Prever índices de criminalidade com base em dados socioeconômicos
- Estimar gastos com saúde a partir de indicadores de saneamento
- Analisar relação entre impostos arrecadados e investimentos públicos

---
