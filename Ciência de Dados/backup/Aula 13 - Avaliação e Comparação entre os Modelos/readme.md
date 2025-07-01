# Semana 7: Avaliação e Comparação entre os Modelos

## Objetivos da Aula
- Realizar uma análise comparativa aprofundada entre os dois algoritmos implementados
- Definir critérios objetivos para seleção do modelo mais adequado
- Otimizar o desempenho dos modelos através de ajustes de hiperparâmetros
- Preparar a documentação técnica da análise comparativa

## Agenda (90 minutos)

### 1. Introdução à Avaliação Comparativa (15 min)
- **Abordagens sistemáticas** para comparação de modelos
- **Métricas de avaliação** apropriadas para cada tipo de problema
- **Trade-offs comuns** entre diferentes algoritmos
- **Princípios de otimização** de modelos

### 2. Workshop de Avaliação Comparativa (60 min)
Durante esta atividade prática, cada grupo realizará uma análise comparativa completa de seus modelos.

#### Roteiro de Avaliação:

1. **Comparação Quantitativa (20 min)**
   - Tabulação das métricas de desempenho para ambos os algoritmos
   - Criação de visualizações comparativas (gráficos de barras, radar, etc.)
   - Análise de diferenças estatísticas (se aplicável)
   - Documentação dos resultados quantitativos

2. **Comparação Qualitativa (15 min)**
   - Análise de interpretabilidade dos modelos
   - Avaliação de robustez e generalização
   - Considerações sobre escalabilidade e manutenção
   - Documentação dos aspectos qualitativos

3. **Otimização de Modelos (25 min)**
   - Identificação de hiperparâmetros críticos para otimização
   - Implementação de técnicas de busca de hiperparâmetros
   - Avaliação do impacto das otimizações
   - Documentação do processo de otimização

### 3. Orientações para Documentação Final e Apresentação (15 min)
- **Estrutura recomendada** para o relatório técnico
- **Diretrizes para apresentação** Lightning Talk
- **Próximos passos** para finalização do projeto
- **Esclarecimento de dúvidas** finais

## Material de Apoio para Otimização de Modelos

### Técnicas de Otimização de Hiperparâmetros

#### 1. Grid Search (Busca em Grade)

```python
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score, r2_score

# Exemplo para algoritmos de classificação
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Criar o modelo base (exemplo com árvore de decisão)
base_model = DecisionTreeClassifier(random_state=42)

# Configurar Grid Search
grid_search = GridSearchCV(
    estimator=base_model,
    param_grid=param_grid,
    cv=5,  # 5-fold cross validation
    scoring='accuracy',
    n_jobs=-1,  # usar todos os processadores disponíveis
    verbose=1
)

# Executar a busca
grid_search.fit(X_train, y_train)

# Melhores parâmetros e score
print(f"Melhores parâmetros: {grid_search.best_params_}")
print(f"Melhor score: {grid_search.best_score_:.4f}")

# Modelo otimizado
best_model = grid_search.best_estimator_

# Avaliar no conjunto de teste
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia no conjunto de teste: {accuracy:.4f}")
```

#### 2. Random Search (Busca Aleatória)

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Exemplo para algoritmos de regressão
param_distributions = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'max_features': uniform(0.1, 0.9)
}

# Criar o modelo base (exemplo com random forest)
base_model = RandomForestRegressor(random_state=42)

# Configurar Random Search
random_search = RandomizedSearchCV(
    estimator=base_model,
    param_distributions=param_distributions,
    n_iter=50,  # número de combinações a testar
    cv=5,  # 5-fold cross validation
    scoring='r2',
    n_jobs=-1,
    verbose=1,
    random_state=42
)

# Executar a busca
random_search.fit(X_train, y_train)

# Melhores parâmetros e score
print(f"Melhores parâmetros: {random_search.best_params_}")
print(f"Melhor score: {random_search.best_score_:.4f}")

# Modelo otimizado
best_model = random_search.best_estimator_

# Avaliar no conjunto de teste
y_pred = best_model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"R² no conjunto de teste: {r2:.4f}")
```

#### 3. Validação Cruzada (Cross-Validation)

```python
from sklearn.model_selection import cross_val_score, KFold

# Definir validação cruzada
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Modelo 1 (exemplo)
model1 = RandomForestClassifier(n_estimators=100, random_state=42)
scores1 = cross_val_score(model1, X, y, cv=cv, scoring='accuracy')
print(f"Modelo 1 - Acurácia média: {scores1.mean():.4f} (±{scores1.std():.4f})")

# Modelo 2 (exemplo)
model2 = GradientBoostingClassifier(n_estimators=100, random_state=42)
scores2 = cross_val_score(model2, X, y, cv=cv, scoring='accuracy')
print(f"Modelo 2 - Acurácia média: {scores2.mean():.4f} (±{scores2.std():.4f})")

# Comparação visual
plt.figure(figsize=(10, 6))
plt.boxplot([scores1, scores2], labels=['Modelo 1', 'Modelo 2'])
plt.title('Comparação de Modelos com Validação Cruzada')
plt.ylabel('Acurácia')
plt.grid(True, alpha=0.3)
plt.show()
```

### Framework para Comparação Sistemática de Modelos

#### 1. Exemplo de Tabela Comparativa Completa

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import time

# Função para avaliar modelos de classificação
def evaluate_classification_models(models, X_train, X_test, y_train, y_test):
    results = {
        'Modelo': [],
        'Acurácia': [],
        'Precisão': [],
        'Recall': [],
        'F1-Score': [],
        'AUC-ROC': [],
        'Tempo de Treinamento': [],
        'Tempo de Inferência': []
    }
    
    for name, model in models.items():
        # Treinar o modelo e medir o tempo
        start_time = time.time()
        model.fit(X_train, y_train)
        train_time = time.time() - start_time
        
        # Fazer predições e medir o tempo
        start_time = time.time()
        y_pred = model.predict(X_test)
        inference_time = time.time() - start_time
        
        # Calcular probabilidades para AUC-ROC
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
            auc = roc_auc_score(y_test, y_prob)
        else:
            auc = np.nan
        
        # Calcular métricas
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted')
        rec = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # Armazenar resultados
        results['Modelo'].append(name)
        results['Acurácia'].append(acc)
        results['Precisão'].append(prec)
        results['Recall'].append(rec)
        results['F1-Score'].append(f1)
        results['AUC-ROC'].append(auc)
        results['Tempo de Treinamento'].append(train_time)
        results['Tempo de Inferência'].append(inference_time)
    
    # Criar DataFrame com os resultados
    return pd.DataFrame(results)

# Função para avaliar modelos de regressão
def evaluate_regression_models(models, X_train, X_test, y_train, y_test):
    results = {
        'Modelo': [],
        'MSE': [],
        'RMSE': [],
        'MAE': [],
        'R²': [],
        'Tempo de Treinamento': [],
        'Tempo de Inferência': []
    }
    
    for name, model in models.items():
        # Treinar o modelo e medir o tempo
        start_time = time.time()
        model.fit(X_train, y_train)
        train_time = time.time() - start_time
        
        # Fazer predições e medir o tempo
        start_time = time.time()
        y_pred = model.predict(X_test)
        inference_time = time.time() - start_time
        
        # Calcular métricas
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Armazenar resultados
        results['Modelo'].append(name)
        results['MSE'].append(mse)
        results['RMSE'].append(rmse)
        results['MAE'].append(mae)
        results['R²'].append(r2)
        results['Tempo de Treinamento'].append(train_time)
        results['Tempo de Inferência'].append(inference_time)
    
    # Criar DataFrame com os resultados
    return pd.DataFrame(results)

# Exemplo de uso para classificação
models_classification = {
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42)
}

results_classification = evaluate_classification_models(
    models_classification, X_train, X_test, y_train, y_test
)

# Visualizar resultados em tabela
print("Resultados da Classificação:")
print(results_classification.round(4))

# Visualizar métricas principais em gráfico
plt.figure(figsize=(12, 6))
metrics = ['Acurácia', 'Precisão', 'Recall', 'F1-Score']
results_classification[metrics].plot(kind='bar')
plt.title('Comparação de Métricas de Classificação')
plt.ylabel('Valor')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# Exemplo similar para regressão...
```

#### 2. Gráfico de Radar para Comparação Visual

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dados de exemplo (normalizar métricas para escala 0-1)
metrics = ['Acurácia', 'Precisão', 'Recall', 'F1-Score', 'AUC-ROC', 
           'Velocidade', 'Interpretabilidade', 'Robustez']
model1_values = [0.85, 0.83, 0.88, 0.85, 0.90, 0.70, 0.50, 0.75]
model2_values = [0.82, 0.90, 0.75, 0.82, 0.85, 0.90, 0.85, 0.65]

# Criar o gráfico de radar
angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]  # Fechar o círculo

model1_values += model1_values[:1]
model2_values += model2_values[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Adicionar eixos (spokes)
plt.xticks(angles[:-1], metrics, size=12)
ax.set_rlabel_position(0)
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], 
           color="grey", size=10)
plt.ylim(0, 1)

# Plotar os modelos
ax.plot(angles, model1_values, 'o-', linewidth=2, label='Modelo 1')
ax.fill(angles, model1_values, alpha=0.1)

ax.plot(angles, model2_values, 'o-', linewidth=2, label='Modelo 2')
ax.fill(angles, model2_values, alpha=0.1)

plt.title('Comparação de Modelos', size=15)
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
```

## Estrutura Recomendada para Relatório Final

### 1. Introdução
- Contexto do problema
- Objetivos do projeto
- Descrição do dataset

### 2. Análise Exploratória de Dados
- Visão geral do dataset
- Visualizações principais
- Insights descobertos
- Pré-processamento realizado

### 3. Implementação dos Algoritmos
- **Algoritmo 1**
  - Descrição e justificativa
  - Implementação e configuração
  - Resultados e métricas
  - Insights específicos

- **Algoritmo 2**
  - Descrição e justificativa
  - Implementação e configuração
  - Resultados e métricas
  - Insights específicos

### 4. Análise Comparativa
- Comparação quantitativa (métricas)
- Comparação qualitativa (interpretabilidade, etc.)
- Pontos fortes e fracos de cada algoritmo
- Recomendação final

### 5. Otimização dos Modelos
- Técnicas de otimização utilizadas
- Resultados da otimização
- Impacto nas métricas de desempenho

### 6. Conclusões e Próximos Passos
- Principais descobertas
- Limitações do projeto
- Sugestões para trabalhos futuros

### 7. Referências
- Fontes de dados
- Artigos e documentações consultadas

## Preparação para a Apresentação Lightning Talk

### Estrutura Recomendada (3 min + 2 min Q&A)

1. **Slide 1: Introdução (30 seg)**
   - Nome do projeto e integrantes
   - Problema abordado
   - Dataset utilizado

2. **Slide 2: Principais Insights da Análise Exploratória (30 seg)**
   - 2-3 descobertas mais relevantes
   - Visualização de maior impacto

3. **Slide 3: Algoritmos Implementados (60 seg)**
   - Algoritmos escolhidos e justificativa
   - Comparação visual das métricas
   - Resultado principal da comparação

4. **Slide 4: Conclusões e Recomendações (60 seg)**
   - Algoritmo recomendado e por quê
   - Principais lições aprendidas
   - Impacto prático dos resultados

### Dicas para a Apresentação

1. **Preparação**
   - Ensaie respeitando o tempo (use cronômetro)
   - Prepare-se para perguntas comuns
   - Tenha slides de backup para questões específicas

2. **Visualização**
   - Priorize gráficos e tabelas claras
   - Use cores contrastantes e fontes grandes
   - Limite o texto ao essencial

3. **Comunicação**
   - Foque nos resultados, não nos detalhes técnicos
   - Explique termos técnicos brevemente
   - Conecte resultados ao problema original

## Entregáveis para a Próxima Aula

Para a Semana 8, cada grupo deve preparar:

1. **Relatório técnico final** seguindo a estrutura recomendada

2. **Apresentação Lightning Talk** com 4-5 slides

3. **Notebook completo** com todo o código, comentários e documentação

## Recursos Adicionais

1. **Otimização de Modelos**:
   - [Hyperparameter Tuning Guide](https://scikit-learn.org/stable/modules/grid_search.html)
   - [Machine Learning Mastery: Hyperparameter Optimization](https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/)
   - [AutoML Options](https://towardsdatascience.com/automl-approaches-in-python-7bd0cf10482e)

2. **Visualização de Comparações**:
   - [RadViz for Model Comparison](https://towardsdatascience.com/radviz-the-ultimate-tool-for-visualizing-multi-variate-data-afc17e3b8b5a)
   - [Seaborn for Statistical Visualization](https://seaborn.pydata.org/examples/index.html)
   - [Effective Data Visualization](https://towardsdatascience.com/effective-data-visualization-in-python-e73fa36e64e5)

3. **Comunicação de Resultados**:
   - [How to Present Machine Learning Results](https://machinelearningmastery.com/present-machine-learning-results/)
   - [Data Storytelling](https://towardsdatascience.com/data-storytelling-a-powerful-tool-for-data-scientists-e8a478cef4e6)
   - [Lightning Talk Guidelines](https://www.semrush.com/blog/how-to-prepare-lightning-talk/)