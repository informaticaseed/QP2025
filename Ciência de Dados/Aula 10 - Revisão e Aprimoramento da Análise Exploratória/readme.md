# Semana 4: Revisão e Aprimoramento da Análise Exploratória

## Objetivos da Aula
- Implementar as melhorias sugeridas no feedback da semana anterior
- Finalizar a análise exploratória dos dados
- Preparar os dados para a fase de modelagem
- Definir os algoritmos a serem implementados

## Agenda (90 minutos)

### 1. Recapitulação e Orientações (20 min)
- **Revisão do feedback** fornecido na semana anterior
- **Dúvidas comuns** identificadas entre os grupos
- **Técnicas avançadas** para análise exploratória:
  - Análise de correlações multivariadas
  - Detecção sistemática de outliers
  - Engenharia de features
  - Visualizações interativas

### 2. Workshop Prático de Revisão (50 min)
Durante esta parte prática, os grupos trabalharão na implementação das melhorias:

#### Atividades Guiadas:
1. **Aprimoramento de Visualizações (15 min)**
   - Melhoria da qualidade técnica dos gráficos
   - Adição de títulos informativos e legendas claras
   - Implementação de paletas de cores apropriadas
   - Criação de visualizações adicionais para insights mais profundos

2. **Preparação para Modelagem (20 min)**
   - Tratamento final de valores ausentes
   - Codificação de variáveis categóricas
   - Normalização/padronização de variáveis numéricas
   - Engenharia de features relevantes

3. **Documentação de Insights (15 min)**
   - Sistematização dos principais insights descobertos
   - Conexão clara entre descobertas e objetivo do projeto
   - Formulação de hipóteses para teste com os algoritmos
   - Documentação de limitações e considerações importantes

### 3. Definição dos Algoritmos (20 min)
- **Apresentação rápida** por grupo dos algoritmos escolhidos (1-2 min cada)
- **Justificativa** para a escolha dos algoritmos
- **Feedback** do professor sobre as escolhas
- **Ajustes finais** no plano de implementação

## Material de Apoio

### Checklist para Finalização da Análise Exploratória

1. **Visualizações Melhoradas**
   - [ ] Gráficos com títulos claros e informativos
   - [ ] Eixos corretamente rotulados com unidades quando aplicável
   - [ ] Paletas de cores apropriadas e acessíveis
   - [ ] Tamanho e resolução adequados
   - [ ] Anotações que destacam pontos importantes

2. **Análise Estatística Completa**
   - [ ] Estatísticas descritivas para todas as variáveis relevantes
   - [ ] Testes de normalidade quando apropriado
   - [ ] Análise de correlação com interpretação clara
   - [ ] Identificação e tratamento adequado de outliers
   - [ ] Análise de tendências temporais (se aplicável)

3. **Preparação para Modelagem**
   - [ ] Dados limpos sem valores ausentes/tratados adequadamente
   - [ ] Variáveis categóricas codificadas (one-hot, label encoding, etc.)
   - [ ] Variáveis numéricas normalizadas/padronizadas
   - [ ] Features irrelevantes removidas
   - [ ] Novas features criadas quando benéfico
   - [ ] Divisão em conjuntos de treino e teste (se já implementando)

4. **Documentação Completa**
   - [ ] Processo de limpeza e transformação documentado
   - [ ] Justificativa para decisões tomadas
   - [ ] Insights principais claramente apresentados
   - [ ] Hipóteses formuladas para modelagem
   - [ ] Limitações e considerações documentadas

### Critérios para Seleção de Algoritmos

Ao escolher os dois algoritmos para implementação, considere:

1. **Adequação ao Problema**
   - O algoritmo é apropriado para o tipo de problema (classificação, regressão, clustering)?
   - O algoritmo funciona bem com o tamanho e estrutura do seu dataset?
   - As suposições do algoritmo são compatíveis com seus dados?

2. **Complementaridade**
   - Os dois algoritmos oferecem abordagens diferentes ao problema?
   - Eles têm pontos fortes e fracos complementares?
   - A comparação entre eles será informativa?

3. **Complexidade e Interpretabilidade**
   - Você consegue entender como o algoritmo funciona?
   - Os resultados serão interpretáveis no contexto do seu problema?
   - A complexidade do algoritmo é justificada para seu caso?

4. **Requisitos Computacionais**
   - O algoritmo é viável considerando o tamanho dos seus dados?
   - Os recursos disponíveis são suficientes para executá-lo?
   - O tempo de treinamento é aceitável para seu contexto?

### Exemplos de Pares Complementares de Algoritmos

**Para Classificação:**
- Árvore de Decisão + Random Forest (simples vs. ensemble)
- Regressão Logística + SVM (linear vs. não-linear)
- KNN + Naive Bayes (baseado em instâncias vs. probabilístico)

**Para Regressão:**
- Regressão Linear + Regressão Polinomial (linear vs. não-linear)
- Ridge/Lasso Regression + Random Forest (regularização vs. ensemble)
- Regressão Linear + SVR (paramétrico vs. não-paramétrico)

**Para Clustering:**
- K-Means + DBSCAN (baseado em centroide vs. baseado em densidade)
- K-Means + Hierarchical Clustering (flat vs. hierárquico)
- DBSCAN + Gaussian Mixture Models (baseado em densidade vs. probabilístico)

## Código de Exemplo: Preparação Final dos Dados

```python
# Exemplo de código para preparação final dos dados
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Carregar dados (substitua pelo seu código)
df = pd.read_csv('seu_dataset.csv')

# Separar features e target
X = df.drop('target_column', axis=1)
y = df['target_column']

# Identificar colunas por tipo
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object', 'category']).columns

# Criar preprocessadores
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combinar preprocessadores
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Criar o pipeline de preparação
prep_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)
])

# Aplicar a transformação
X_preprocessed = prep_pipeline.fit_transform(X)

# Dividir em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X_preprocessed, y, test_size=0.3, random_state=42)

# Agora X_train e X_test estão prontos para os algoritmos
print(f"Forma de X_train: {X_train.shape}")
print(f"Forma de X_test: {X_test.shape}")
```

## Entregáveis para a Próxima Aula

Para a próxima aula (Semana 5), cada grupo deve preparar:

1. **Notebook completo** com a análise exploratória revisada contendo:
   - Visualizações aprimoradas e insights finais
   - Dados completamente preparados para modelagem
   - Documentação clara de todo o processo

2. **Documento de planejamento** (1 página) contendo:
   - Dois algoritmos escolhidos com justificativa
   - Métricas que serão usadas para avaliação
   - Expectativas preliminares de resultados
   - Possíveis desafios na implementação

## Recursos Adicionais Recomendados

1. **Visualizações Avançadas:**
   - [Plotly Express](https://plotly.com/python/plotly-express/) - Para gráficos interativos
   - [Seaborn Advanced Tutorial](https://seaborn.pydata.org/tutorial.html) - Técnicas avançadas
   - [Matplotlib Guidelines](https://matplotlib.org/stable/users/explain/quick_start.html) - Boas práticas

2. **Preparação de Dados:**
   - [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) - Guia oficial
   - [Feature Engineering Guide](https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/) - Técnicas práticas

3. **Seleção de Algoritmos:**
   - [Scikit-learn Algorithm Cheat Sheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) - Mapa de decisão
   - [Machine Learning Algorithms Explained](https://towardsdatascience.com/all-machine-learning-algorithms-explained-in-7-minutes-or-less-c282f145f3ec) - Explicações concisas