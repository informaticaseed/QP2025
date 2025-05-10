Aqui está um plano de aula sobre **Aprendizado Supervisionado** incluindo teoria e uma prática em **Python** para ser usada no **Google Colab**.
# 🎓 **Aula 1: Introdução ao Aprendizado Supervisionado**

## 📌 **Objetivos**
- Compreender o que é Aprendizado de Máquina e Aprendizado Supervisionado.
- Explorar exemplos do dia a dia.
- Implementar uma prática simples em Python.

---

## 🔎 **O que é Aprendizado de Máquina?**
É uma subárea da inteligência artificial (IA) que ensina computadores a aprenderem a partir de dados, sem precisar ser explicitamente programado.

---

## 🤖 **Tipos de Aprendizado de Máquina**
1. **Supervisionado**: Aprende a partir de dados rotulados. Exemplo: classificar e-mails como "spam" ou "não spam".
2. **Não Supervisionado**: Identifica padrões sem rótulos. Exemplo: segmentação de clientes em grupos.
3. **Aprendizado por Reforço**: Aprende com tentativa e erro. Exemplo: IA jogando xadrez.

---

## 🎯 **Foco da Aula: Aprendizado Supervisionado**
No aprendizado supervisionado, o modelo recebe **entradas (X)** e **saídas desejadas (Y)** para aprender padrões e fazer previsões futuras.

### Exemplo no Dia a Dia:
- Gmail classificando e-mails como spam.
- Netflix recomendando filmes baseados no que você assistiu.
- Banco detectando fraudes em transações.

---

## 🏗 **Atividade Prática: Criando um Modelo de Classificação**

### 📌 **Objetivo**
Criar um modelo simples para classificar **comentários como positivos ou negativos**.

### 📜 **Passos**
1. Criar uma base de dados com frases e seus respectivos sentimentos.
2. Treinar um modelo de Machine Learning usando `scikit-learn`.
3. Testar o modelo com novas frases.

### ⚡ **Código para Google Colab**
Copie e cole no **Google Colab** para rodar diretamente.

```python
# Instalar bibliotecas necessárias (caso não estejam instaladas)
!pip install scikit-learn

# Importar bibliotecas
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 📌 1. Criar a base de dados de treinamento
textos = np.array([
    "Eu adorei esse filme", "O filme foi incrível!", "Que filme horrível!",
    "Eu odiei a comida", "Esse lugar é maravilhoso", "O atendimento foi péssimo",
    "Ótimo produto, recomendo!", "Muito ruim, não gostei", "Super recomendo!",
    "Não vale a pena comprar", "A experiência foi fantástica!", "O pior serviço que já tive"
])
sentimentos = np.array(["positivo", "positivo", "negativo", "negativo", "positivo", "negativo",
                         "positivo", "negativo", "positivo", "negativo", "positivo", "negativo"])

# 📌 2. Separar os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(textos, sentimentos, test_size=0.2, random_state=42)

# 📌 3. Criar pipeline de processamento e modelo
modelo = Pipeline([
    ('vectorizer', CountVectorizer()),  # Converte texto em números
    ('classifier', MultinomialNB())  # Algoritmo de classificação
])

# 📌 4. Treinar o modelo
modelo.fit(X_train, y_train)

# 📌 5. Avaliar modelo
accuracy = modelo.score(X_test, y_test)
print(f"Acurácia do modelo: {accuracy:.2%}")

# 📌 6. Testar com frases novas
novos_textos = ["Amei esse restaurante", "Não gostei do filme", "O serviço foi excelente"]
predicoes = modelo.predict(novos_textos)

for texto, sentimento in zip(novos_textos, predicoes):
    print(f"Frase: '{texto}' -> Classificação: {sentimento}")
```

---

## 📊 **Discussão em Sala**
1. O que o modelo aprendeu?
2. Ele errou alguma previsão? Por quê?
3. Como podemos melhorá-lo?
4. Como modelos como o ChatGPT são treinados comparado a esse modelo simples?

---

## 🎯 **Desafio para os Alunos**
1. Adicione novas frases à base de dados e veja como o modelo se comporta.
2. Teste frases ambíguas e observe como ele classifica.
3. Pesquise sobre outras abordagens de aprendizado supervisionado.

---