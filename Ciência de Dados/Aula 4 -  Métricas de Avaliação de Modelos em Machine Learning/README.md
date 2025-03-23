# 📊 Métricas de Avaliação de Modelos em Machine Learning

## 📌 Objetivos da Aula
- Entender como avaliar se um modelo de machine learning está funcionando bem
- Conhecer a matriz de confusão e suas métricas principais
- Implementar um modelo simples e avaliar seu desempenho usando Python

## 🔎 Conceitos Fundamentais

### Matriz de Confusão
Uma tabela que nos mostra os acertos e erros do nosso modelo de classificação:

```
               │ Predito Positivo │ Predito Negativo
─────────────────────────────────────────────────────
Real Positivo  │     ACERTOU!     │      ERROU!
     (VP)      │                  │       (FN)
─────────────────────────────────────────────────────
Real Negativo  │      ERROU!      │     ACERTOU!
     (FP)      │                  │       (VN)
```

## 🎯 Analogias do Dia a Dia

### Matriz de Confusão = Boletim do Modelo
```
📝 Como ler as notas do seu modelo:

✅ Verdadeiro Positivo = Acertou que era SPAM
❌ Falso Positivo = Disse que era SPAM, mas não era
❌ Falso Negativo = Não viu o SPAM que existia
✅ Verdadeiro Negativo = Acertou que não era SPAM
```

### Métricas = Notas em Diferentes Matérias
- **Acurácia** = Nota geral
- **Precisão** = Nota em não dar alarmes falsos
- **Recall** = Nota em encontrar todos os problemas
- **F1-Score** = Média entre precisão e recall

### Métricas Principais
- **Acurácia**: Porcentagem total de acertos do modelo
  - `(VP + VN) / Total`
- **Precisão**: Dos que o modelo disse que são positivos, quantos realmente são?
  - `VP / (VP + FP)`
- **Recall**: Dos casos realmente positivos, quantos o modelo encontrou?
  - `VP / (VP + FN)`
- **F1-Score**: Equilíbrio entre precisão e recall
  - `2 * (Precisão * Recall) / (Precisão + Recall)`

## 💻 Exemplo Prático em Python

```python
# Importar bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Criar um conjunto de dados simulado (para classificação)
X, y = make_classification(n_samples=1000, n_features=4, random_state=42)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Calcular a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(conf_matrix)

# Calcular métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"\nAcurácia: {accuracy:.2f}")
print(f"Precisão: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")

# Visualizar a matriz de confusão
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, cmap='Blues')
plt.title('Matriz de Confusão')
plt.colorbar()
plt.xlabel('Predito')
plt.ylabel('Real')
plt.xticks([0, 1], ['Negativo', 'Positivo'])
plt.yticks([0, 1], ['Negativo', 'Positivo'])

# Adicionar valores à matriz
thresh = conf_matrix.max() / 2
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        plt.text(j, i, conf_matrix[i, j],
                 ha="center", va="center",
                 color="white" if conf_matrix[i, j] > thresh else "black")
plt.show()
```

## 🎯 Atividade Prática para os Alunos

### Objetivo
Criar um modelo para classificar mensagens como spam ou não-spam e avaliar seu desempenho.

### Código Base para os Alunos

```python
# Importar bibliotecas
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Criar um conjunto de dados simples (mensagens e classificações)
mensagens = [
    "PARABÉNS! Você ganhou um iPhone grátis!", 
    "Olá, tudo bem? Vamos nos encontrar amanhã?",
    "URGENTE: Sua conta foi bloqueada. Clique aqui para desbloquear",
    "Lembrete: reunião amanhã às 10h",
    "GANHE DINHEIRO RÁPIDO! Clique neste link agora!",
    "Oi, você deixou seu casaco aqui ontem",
    "PROMOÇÃO EXCLUSIVA: 70% de desconto em todos os produtos!",
    "Confirmo nosso almoço de amanhã",
    "ATENÇÃO: Última chance para regularizar seu CPF!",
    "Me avisa quando chegar em casa"
]

# 0 = normal, 1 = spam
rotulos = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Transformar textos em números (vetorização)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mensagens)
y = rotulos

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# TODO: Calcular a matriz de confusão e as métricas
# 1. Calcule a matriz de confusão
conf_matrix = ...

# 2. Calcule acurácia, precisão, recall e f1-score
acuracia = ...
precisao = ...
recall = ...
f1 = ...

# 3. Imprima os resultados
print("Matriz de Confusão:")
print(...)
print(f"Acurácia: {acuracia:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")

# 4. BÔNUS: Teste o modelo com novas mensagens
novas_mensagens = [
    "Oi, como você está?",
    "CLIQUE AGORA E GANHE R$1000!"
]
# Transformar as novas mensagens
X_novas = ...
# Prever
previsoes = ...
# Mostrar resultados
for mensagem, previsao in zip(novas_mensagens, previsoes):
    resultado = "SPAM" if previsao == 1 else "NÃO SPAM"
    print(f"Mensagem: '{mensagem}' → Classificação: {resultado}")
```

## 🎮 Exercícios Gamificados
Imagine que você é um detetive de spam:
1. **Nível 1**: Calcule a acurácia
2. **Nível 2**: Descubra a precisão
3. **Boss Fight**: Equilibre precisão e recall

## 📝 Exercícios de Avaliação

1. **Complete as frases:**
   - A métrica que mede a proporção total de acertos é chamada de __________.
   - __________ mede a proporção de exemplos positivos identificados corretamente.
   - Quando queremos equilibrar precisão e recall, usamos a métrica __________.

2. **Interpretando a Matriz:**
   Considere a seguinte matriz de confusão:
   ```
   [50  10]
   [5   35]
   ```
   a) Quantos verdadeiros positivos existem?
   b) Calcule a acurácia do modelo.
   c) Calcule a precisão do modelo.

3. **Questão Prática:**
   No exemplo de detecção de spam, por que o recall pode ser mais importante que a precisão? Ou a precisão pode ser mais importante que o recall? Explique.

4. **Desafio:**
   Modifique o código da atividade prática adicionando pelo menos 5 novas mensagens (inventadas por você) ao conjunto de dados. Como isso afeta as métricas do modelo?

## 📚 Dicas para Estudar para Concursos
- Memorize as fórmulas das métricas principais (acurácia, precisão, recall, F1)
- Entenda quando usar cada métrica (casos de classes desbalanceadas, custos diferentes de erro)
- Pratique o cálculo manual das métricas a partir de uma matriz de confusão
- Saiba interpretar os resultados: um modelo com alta precisão e baixo recall significa que ele é "conservador" (poucos falsos positivos)

## 🎓 Material de Referência
- [Documentação do Scikit-learn sobre métricas](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Guia ilustrado sobre matriz de confusão](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)