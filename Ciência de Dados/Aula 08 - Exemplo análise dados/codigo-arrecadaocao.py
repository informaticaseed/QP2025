import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('arrecadacao.csv')

# Escolher a variável que queremos prever (exemplo: receita_previdenciaria)
variavel_alvo = 'receita_previdenciaria'

# Preparar os dados para o modelo
# Codificar a variável categórica (estados)
encoder = OneHotEncoder(sparse_output=False)
estados_codificados = encoder.fit_transform(df[['sigla_uf']])
colunas_estados = encoder.get_feature_names_out(['estado'])
df_estados = pd.DataFrame(estados_codificados, columns=colunas_estados)

# Combinar dados originais com estados codificados
df_completo = pd.concat([df.reset_index(drop=True), df_estados], axis=1)

# Selecionar features para o modelo
features = ['ano', 'mes'] + list(colunas_estados)
X = df_completo[features]
y = df_completo[variavel_alvo]

# Dividir em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Avaliar o modelo
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Erro Quadrático Médio: {mse}')
print(f'Coeficiente de Determinação (R²): {r2}')

# Prever dados para 2026
# Criar um dataframe para 2026 (todos os meses para todos os estados)
df_previsao = pd.DataFrame()
estados = df['sigla_uf'].unique()

for estado in estados:
    for mes in range(1, 13):
        df_temp = pd.DataFrame({'ano': [2026], 'mes': [mes], 'sigla_uf': [estado]})
        df_previsao = pd.concat([df_previsao, df_temp], ignore_index=True)

# Codificar os estados para previsão
estados_prev_codificados = encoder.transform(df_previsao[['sigla_uf']])
df_estados_prev = pd.DataFrame(estados_prev_codificados, columns=colunas_estados)
df_previsao = pd.concat([df_previsao.reset_index(drop=True), df_estados_prev], axis=1)

# Selecionar features para previsão
X_prev = df_previsao[features]

# Fazer as previsões
previsoes = modelo.predict(X_prev)
df_previsao[variavel_alvo] = previsoes

# Exibir as previsões
print('\nPrevisões para 2026:')
print(df_previsao[['ano', 'mes', 'sigla_uf', variavel_alvo]].head(24))