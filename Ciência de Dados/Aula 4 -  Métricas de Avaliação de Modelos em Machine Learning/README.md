# 📊 Métricas de Avaliação de Modelos em Machine Learning

## 📌 Objetivos da Aula
- Entender como avaliar se um modelo de machine learning está funcionando bem
- Conhecer a matriz de confusão e suas métricas principais
- Implementar um modelo simples e avaliar seu desempenho usando Python

## 🔎 Conceitos Fundamentais

### Matriz de Confusão
Uma tabela que mostra os acertos e erros do nosso modelo de classificação:

```
               │ Predito Positivo │ Predito Negativo
─────────────────────────────────────────────────────
Real Positivo  │     ACERTOU!     │      ERROU!
               │        (VP)      │       (FN)
─────────────────────────────────────────────────────
Real Negativo  │      ERROU!      │     ACERTOU!
               │         (FP)     │       (VN)
```

### Analogia Prática: Detector de Spam
- **Verdadeiro Positivo (VP):** Email é spam e o sistema detectou corretamente
- **Falso Positivo (FP):** Email normal que o sistema marcou incorretamente como spam
- **Falso Negativo (FN):** Email spam que o sistema não detectou (deixou passar)
- **Verdadeiro Negativo (VN):** Email normal que o sistema corretamente deixou na caixa de entrada

### Métricas Principais
- **Acurácia**: Porcentagem total de acertos do modelo
  - `(VP + VN) / (VP + VN + FP + FN)`
- **Precisão**: Dos emails que o modelo classificou como spam, quantos realmente eram spam?
  - `VP / (VP + FP)`
- **Recall**: Dos emails que eram realmente spam, quantos o modelo conseguiu identificar?
  - `VP / (VP + FN)`
- **F1-Score**: Equilíbrio entre precisão e recall
  - `2 * (Precisão * Recall) / (Precisão + Recall)`

## 📝 Exercícios de Cálculo

### Exercício 1
Um sistema de detecção de spam analisou 100 emails com os seguintes resultados:
- 45 emails eram spam e foram detectados corretamente
- 5 emails normais foram classificados como spam
- 15 emails spam não foram detectados
- 35 emails normais foram classificados corretamente

**Calcule:**
a) Preencha a matriz de confusão
b) Calcule a acurácia
c) Calcule a precisão
d) Calcule o recall
e) Calcule o F1-score

### Exercício 2
Um modelo de diagnóstico médico foi testado com 200 pacientes:

```
               │ Predito Doente │ Predito Saudável
─────────────────────────────────────────────────────
Real Doente    │       80       │        20
─────────────────────────────────────────────────────
Real Saudável  │       30       │        70
```

**Calcule:**
a) A acurácia do modelo
b) A precisão (considerando "doente" como positivo)
c) O recall
d) O F1-score
e) Se você fosse médico, preferiria um modelo com alta precisão ou alto recall? Por quê?

### Exercício 3
Considere a seguinte matriz de confusão:
```
[35  5]
[10 50]
```

**Calcule:**
a) O total de exemplos analisados
b) A acurácia do modelo
c) A precisão
d) O recall
e) O F1-score

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
import matplotlib.pyplot as plt

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
conf_matrix = confusion_matrix(y_test, y_pred)

# 2. Calcule acurácia, precisão, recall e f1-score
acuracia = accuracy_score(y_test, y_pred)
precisao = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# 3. Imprima os resultados
print("Matriz de Confusão:")
print(conf_matrix)
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
X_novas = vectorizer.transform(novas_mensagens)
# Prever
previsoes = modelo.predict(X_novas)
# Mostrar resultados
for mensagem, previsao in zip(novas_mensagens, previsoes):
    resultado = "SPAM" if previsao == 1 else "NÃO SPAM"
    print(f"Mensagem: '{mensagem}' → Classificação: {resultado}")

# 5. Visualizar a matriz de confusão
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, cmap='Blues')
plt.title('Matriz de Confusão')
plt.colorbar()
plt.xlabel('Predito')
plt.ylabel('Real')
plt.xticks([0, 1], ['Não-Spam', 'Spam'])
plt.yticks([0, 1], ['Não-Spam', 'Spam'])

# Adicionar valores à matriz
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        plt.text(j, i, conf_matrix[i, j],
                ha="center", va="center",
                color="white" if conf_matrix[i, j] > 1 else "black")
plt.show()
```

## 📝 Atividades de Avaliação

### Atividade 1: Cálculo de Métricas
Considere a seguinte matriz de confusão:
```
[120  30]
[ 20  80]
```

1. Identifique os valores de VP, FP, FN e VN
2. Calcule a acurácia
3. Calcule a precisão
4. Calcule o recall
5. Calcule o F1-score

### Atividade 2: Interpretação
Para cada cenário abaixo, indique qual métrica seria mais importante priorizar:

1. Sistema de detecção de fraudes bancárias (falsos negativos são muito prejudiciais)
2. Sistema de filtro de spam (falsos positivos são muito prejudiciais)
3. Sistema de recomendação de produtos em um site (equilíbrio é importante)
4. Sistema de diagnóstico de uma doença grave (falsos negativos são muito prejudiciais)

### Atividade 3: Desafio
1. Adicione 5 novas mensagens ao conjunto de dados (com seus respectivos rótulos)
2. Recalcule as métricas e compare com os resultados anteriores
3. Explique como suas novas mensagens afetaram o desempenho do modelo

## 📚 Material de Referência
- [Documentação do Scikit-learn sobre métricas](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Guia ilustrado sobre matriz de confusão](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)

## 🔑 Gabarito dos Exercícios de Cálculo

### Exercício 1
a) Matriz de Confusão:
```
VP = 45, FN = 15
FP = 5,  VN = 35
```
b) Acurácia = (45 + 35) / 100 = 0,80 = 80%
c) Precisão = 45 / (45 + 5) = 0,90 = 90%
d) Recall = 45 / (45 + 15) = 0,75 = 75%
e) F1 = 2 * (0,90 * 0,75) / (0,90 + 0,75) = 0,82 = 82%

### Exercício 2
a) Acurácia = (80 + 70) / 200 = 0,75 = 75%
b) Precisão = 80 / (80 + 30) = 0,73 = 73%
c) Recall = 80 / (80 + 20) = 0,80 = 80%
d) F1 = 2 * (0,73 * 0,80) / (0,73 + 0,80) = 0,76 = 76%

### Exercício 3
a) Total = 35 + 5 + 10 + 50 = 100 exemplos
b) Acurácia = (35 + 50) / 100 = 0,85 = 85%
c) Precisão = 35 / (35 + 10) = 0,78 = 78%
d) Recall = 35 / (35 + 5) = 0,88 = 88%
e) F1 = 2 * (0,78 * 0,88) / (0,78 + 0,88) = 0,83 = 83%