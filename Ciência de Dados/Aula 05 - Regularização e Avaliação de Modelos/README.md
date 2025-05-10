# 🎯 Regularização e Avaliação de Modelos em Machine Learning

## 📌 Objetivos da Aula
- Compreender o conceito de regularização e sua importância
- Conhecer os principais tipos de regularização (L1 e L2)
- Entender como evitar overfitting usando regularização
- Implementar modelos com regularização usando Python

## 🔎 Conceitos Fundamentais

### Overfitting x Underfitting
- **Overfitting**: modelo "decorou" os dados de treino
- **Underfitting**: modelo muito simples, não aprendeu o suficiente

### Regularização
Técnica para evitar overfitting adicionando penalidades aos parâmetros do modelo.

### 📱 Analogia Simples
Pense na regularização como um "controle parental" para seu modelo:
- **Sem regularização**: Modelo pode fazer o que quiser (memorizar tudo)
- **Com regularização**: Modelo tem limites e aprende o que é realmente importante

### 🎮 Exemplos do Dia a Dia
- **Overfitting** é como decorar as respostas da prova sem entender a matéria
- **Underfitting** é como chutar todas as respostas sem estudar
- **Regularização** é como estudar de forma equilibrada

#### Tipos Principais
1. **L1 (Lasso)**
   - Adiciona |β| à função de custo
   - Pode zerar coeficientes (seleção de features)
   - Bom para features esparsas

2. **L2 (Ridge)**
   - Adiciona β² à função de custo
   - Diminui coeficientes, mas não zera
   - Mais estável que L1

3. **Elastic Net**
   - Combina L1 e L2
   - Melhor dos dois mundos

## 💻 Exemplo Prático em Python

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, Lasso, ElasticNet
import matplotlib.pyplot as plt

# Criar dados sintéticos
np.random.seed(42)
X = np.random.randn(100, 20)  # 100 amostras, 20 features
y = X[:, 0] * 2 + X[:, 1] * (-1.5) + np.random.randn(100) * 0.1  # Apenas 2 features são relevantes

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinar modelos com diferentes regularizações
modelos = {
    'Ridge': Ridge(alpha=1.0),
    'Lasso': Lasso(alpha=1.0),
    'ElasticNet': ElasticNet(alpha=1.0, l1_ratio=0.5)
}

# Treinar e avaliar cada modelo
for nome, modelo in modelos.items():
    # Treinar
    modelo.fit(X_train_scaled, y_train)
    
    # Avaliar
    score = modelo.score(X_test_scaled, y_test)
    print(f'\n{nome}:')
    print(f'R² Score: {score:.3f}')
    print('Coeficientes diferentes de zero:', np.sum(modelo.coef_ != 0))
    
    # Visualizar coeficientes
    plt.figure(figsize=(10, 4))
    plt.bar(range(20), modelo.coef_)
    plt.title(f'Coeficientes do modelo {nome}')
    plt.xlabel('Feature')
    plt.ylabel('Coeficiente')
    plt.show()
```

## 🎯 Atividade Prática para os Alunos

### Objetivo
Comparar diferentes tipos de regularização em um problema de previsão de preços de casas.

### Base de Dados
```python
from sklearn.datasets import fetch_california_housing

# Carregar dados
housing = fetch_california_housing()
X, y = housing.data, housing.target

# TODO: 
# 1. Dividir em treino/teste
# 2. Normalizar os dados
# 3. Treinar modelos com Ridge, Lasso e ElasticNet
# 4. Comparar resultados
# 5. Visualizar coeficientes
```

## 📝 Exercícios Teóricos

1. O que é regularização e por que é importante?

2. Complete:
   - Regularização L1 é conhecida como ________ e tende a ________ alguns coeficientes.
   - Regularização L2 é conhecida como ________ e tende a ________ todos os coeficientes.

3. Qual a principal diferença entre L1 e L2? Quando usar cada uma?

4. Como o parâmetro alpha afeta a regularização?

## 🔬 Questões Práticas

1. **Caso Prático**: Em um modelo de previsão de vendas com 1000 features, muitas são irrelevantes. Qual regularização você usaria e por quê?

2. **Análise**: Dado o gráfico de coeficientes abaixo, qual regularização foi provavelmente usada?
```
Coeficientes: [0, 2.5, 0, 1.8, 0, 0, 3.1, 0, 0, 0]
```

3. **Implementação**: Modifique o código da atividade prática para testar diferentes valores de alpha. Como isso afeta os resultados?

## 🎓 Conceitos-Chave para Memorizar

### Regularização L1 (Lasso)
- Fórmula: L1 = Σ|βi|
- Características:
  - Seleção de features
  - Solução esparsa
  - Bom para features redundantes

### Regularização L2 (Ridge)
- Fórmula: L2 = Σ(βi)²
- Características:
  - Reduz multicolinearidade
  - Solução mais estável
  - Mantém todas as features

### Elastic Net
- Fórmula: α(λ||β||₁ + (1-λ)||β||₂²)
- Características:
  - Combina L1 e L2
  - λ controla o mix
  - Mais flexível

## 💡 Dicas de Estudo
1. **Visualize os conceitos**:
   - L1 (Lasso) = ✂️ Tesoura (corta features)
   - L2 (Ridge) = 🔨 Martelo (amassa valores)
   - Elastic Net = 🛠️ Canivete suíço (faz os dois)

2. **Quando usar cada tipo**:
   ```
   Muitas features irrelevantes? → Use L1 (Lasso)
   Features correlacionadas? → Use L2 (Ridge)
   Não tem certeza? → Use Elastic Net
   ```

## 📚 Material Extra
- [Scikit-learn: Regularização](https://scikit-learn.org/stable/modules/regularization.html)
- [Analytics Vidhya: Regularização](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/)
- [Towards Data Science: L1 vs L2](https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c)
