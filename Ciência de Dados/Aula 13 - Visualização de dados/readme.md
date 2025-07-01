# 📊 Aula 13: Visualização Avançada de Dados - Contando Histórias com Gráficos

## ⏱️ Cronograma da Aula (50 min)
* **(10 min) Introdução:** Princípios da boa visualização
* **(15 min) Demonstração:** Transformando tabelas em insights visuais
* **(20 min) Prática:** Criando gráficos eficazes em Python
* **(5 min) Desafio:** Melhorar um gráfico existente

## 🎯 Objetivo da Aula
Aprender técnicas para criar visualizações impactantes que comuniquem insights de forma clara e persuasiva.

## 🧠 Conceito Fundamental
Uma boa visualização transforma números em insights visuais que qualquer pessoa pode entender rapidamente.

## 🎬 Analogia do Cinema
**"Seu Dado é o Roteiro, Sua Visualização é o Filme"**:
- Dados brutos são como o roteiro escrito (poucos conseguem imaginar o filme)
- Visualizações são como o filme finalizado (todos entendem a história)
- Boas visualizações, como bons filmes, capturam atenção e transmitem mensagens

## 💻 Vamos Praticar no Colab!

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o visual
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("deep")
plt.rcParams['font.size'] = 12

# DADOS: Crescimento de usuários de redes sociais (em milhões)
dados = {
    'Ano': [2018, 2019, 2020, 2021, 2022, 2023],
    'Instagram': [800, 1000, 1200, 1400, 1600, 1800],
    'TikTok': [300, 500, 800, 1200, 1500, 1700],
    'Facebook': [2200, 2400, 2500, 2600, 2700, 2800],
    'Twitter': [330, 350, 390, 400, 410, 420]
}
df = pd.DataFrame(dados)

# 1. GRÁFICO BÁSICO (ruim)
plt.figure(figsize=(10, 6))
plt.plot(df['Ano'], df['Instagram'])
plt.plot(df['Ano'], df['TikTok'])
plt.plot(df['Ano'], df['Facebook'])
plt.plot(df['Ano'], df['Twitter'])
plt.title('Usuários de Redes Sociais')
plt.show()

# 2. GRÁFICO MELHORADO (bom)
plt.figure(figsize=(12, 7))

# Linhas mais grossas, com marcadores e cores distintas
plt.plot(df['Ano'], df['Instagram'], marker='o', linewidth=3, label='Instagram', color='#C13584')
plt.plot(df['Ano'], df['TikTok'], marker='s', linewidth=3, label='TikTok', color='#69C9D0')
plt.plot(df['Ano'], df['Facebook'], marker='^', linewidth=3, label='Facebook', color='#3b5998')
plt.plot(df['Ano'], df['Twitter'], marker='d', linewidth=3, label='Twitter', color='#1DA1F2')

# Título informativo
plt.title('Crescimento de Usuários de Redes Sociais (2018-2023)', fontsize=16, pad=20)

# Rótulos claros
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Número de Usuários (milhões)', fontsize=14)

# Grade mais leve
plt.grid(True, alpha=0.3)

# Legenda em posição estratégica
plt.legend(fontsize=12, loc='upper left')

# Anotação destacando um insight importante
plt.annotate('Boom do TikTok\nna pandemia', 
             xy=(2020, 800),  # Ponto que estamos anotando
             xytext=(2019, 1100),  # Onde o texto vai aparecer
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=12,
             bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.7))

plt.tight_layout()
plt.show()

# 3. GRÁFICO DE BARRAS COMPARATIVO
# Vamos comparar 2018 vs 2023
df_comparacao = df[df['Ano'].isin([2018, 2023])].copy()
df_comparacao_melted = pd.melt(df_comparacao, 
                              id_vars=['Ano'], 
                              value_vars=['Instagram', 'TikTok', 'Facebook', 'Twitter'],
                              var_name='Rede Social', value_name='Usuários (milhões)')

plt.figure(figsize=(12, 7))
sns.barplot(x='Rede Social', y='Usuários (milhões)', hue='Ano', data=df_comparacao_melted, palette=['#aaaaaa', '#ff9933'])

# Título e rótulos
plt.title('Comparação de Usuários: 2018 vs 2023', fontsize=16, pad=20)
plt.xlabel('Rede Social', fontsize=14)
plt.ylabel('Número de Usuários (milhões)', fontsize=14)

# Adicionar os valores nas barras
for i, p in enumerate(plt.gca().patches):
    height = p.get_height()
    plt.text(p.get_x() + p.get_width()/2., height + 50,
            f'{int(height)}M',
            ha="center", fontsize=11, fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# 4. GRÁFICO DE CRESCIMENTO PERCENTUAL
# Calcular crescimento percentual de 2018 a 2023
crescimento = pd.DataFrame({
    'Rede Social': ['Instagram', 'TikTok', 'Facebook', 'Twitter'],
    'Crescimento (%)': [
        (df['Instagram'].iloc[-1] / df['Instagram'].iloc[0] - 1) * 100,
        (df['TikTok'].iloc[-1] / df['TikTok'].iloc[0] - 1) * 100,
        (df['Facebook'].iloc[-1] / df['Facebook'].iloc[0] - 1) * 100,
        (df['Twitter'].iloc[-1] / df['Twitter'].iloc[0] - 1) * 100
    ]
})
crescimento = crescimento.sort_values('Crescimento (%)', ascending=False)

plt.figure(figsize=(12, 7))
bars = sns.barplot(x='Rede Social', y='Crescimento (%)', data=crescimento, palette='viridis')

# Destacar a barra de maior crescimento
bars.patches[0].set_facecolor('#ff9933')

# Título e rótulos
plt.title('Crescimento Percentual por Rede Social (2018-2023)', fontsize=16, pad=20)
plt.xlabel('Rede Social', fontsize=14)
plt.ylabel('Crescimento (%)', fontsize=14)

# Adicionar os valores nas barras
for i, p in enumerate(plt.gca().patches):
    height = p.get_height()
    plt.text(p.get_x() + p.get_width()/2., height + 5,
            f'{int(height)}%',
            ha="center", fontsize=12, fontweight='bold')

# Adicionar linha horizontal em 0%
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# 5. DASHBOARD COMPLETO
# Criando um dashboard com vários gráficos
plt.figure(figsize=(18, 12))

# Título do dashboard
plt.suptitle('DASHBOARD: EVOLUÇÃO DAS REDES SOCIAIS (2018-2023)', fontsize=20, y=0.98, fontweight='bold')

# Gráfico 1: Linhas de crescimento
plt.subplot(2, 2, 1)
for rede, cor in zip(['Instagram', 'TikTok', 'Facebook', 'Twitter'], ['#C13584', '#69C9D0', '#3b5998', '#1DA1F2']):
    plt.plot(df['Ano'], df[rede], marker='o', linewidth=2.5, label=rede, color=cor)
plt.title('Crescimento de Usuários', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Milhões de Usuários', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# Gráfico 2: Comparação 2018 vs 2023
plt.subplot(2, 2, 2)
sns.barplot(x='Rede Social', y='Usuários (milhões)', hue='Ano', data=df_comparacao_melted, palette=['#aaaaaa', '#ff9933'])
plt.title('2018 vs 2023', fontsize=14)
plt.xlabel('Rede Social', fontsize=12)
plt.ylabel('Milhões de Usuários', fontsize=12)
plt.legend(title='Ano', fontsize=10)

# Gráfico 3: Crescimento percentual
plt.subplot(2, 2, 3)
sns.barplot(x='Rede Social', y='Crescimento (%)', data=crescimento, palette='viridis')
plt.title('Crescimento Percentual', fontsize=14)
plt.xlabel('Rede Social', fontsize=12)
plt.ylabel('Crescimento (%)', fontsize=12)
for i, p in enumerate(plt.gca().patches):
    height = p.get_height()
    plt.text(p.get_x() + p.get_width()/2., height + 5, f'{int(height)}%', ha="center", fontsize=10)
    
# Gráfico 4: Participação de mercado (pizza)
plt.subplot(2, 2, 4)
mercado_2023 = df.iloc[-1][['Instagram', 'TikTok', 'Facebook', 'Twitter']]
cores = ['#C13584', '#69C9D0', '#3b5998', '#1DA1F2']
plt.pie(mercado_2023, labels=mercado_2023.index, autopct='%1.1f%%', colors=cores, startangle=90)
plt.title('Participação de Mercado (2023)', fontsize=14)
plt.axis('equal')  # Para garantir que o gráfico seja um círculo

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
```

## 📊 Princípios para Visualizações Eficazes

1. **Conheça seu público**
   - Adapte a complexidade ao conhecimento técnico da audiência
   - Use termos e exemplos familiares

2. **Escolha o gráfico certo**
   - **Barras**: para comparações entre categorias
   - **Linhas**: para tendências ao longo do tempo
   - **Dispersão**: para relações entre variáveis
   - **Pizza**: para proporções (use apenas com poucas categorias!)
   - **Mapas de calor**: para correlações ou dados tabulares
   - **Boxplot**: para distribuições e outliers

3. **Simplifique**
   - Remova elementos desnecessários
   - Destaque apenas informações importantes
   - Use títulos claros e diretos

4. **Use cores estrategicamente**
   - Cores devem ter significado, não apenas decoração
   - Considere pessoas com daltonismo (evite vermelho-verde)
   - Use paletas harmoniosas

5. **Conte uma história**
   - Organize visualizações em sequência lógica
   - Destaque insights principais com anotações
   - Conecte os pontos para o espectador

## 📝 Exercício Prático
Use o dataset de notas escolares abaixo para criar:
1. Um gráfico de barras comparando as notas médias por disciplina
2. Um gráfico de linhas mostrando a evolução das notas ao longo dos bimestres
3. Um dashboard combinando pelo menos dois gráficos diferentes

```python
notas = {
    'Disciplina': ['Matemática', 'Português', 'Ciências', 'História', 'Geografia'],
    'Bimestre1': [7.5, 8.0, 7.0, 6.5, 7.0],
    'Bimestre2': [6.5, 7.5, 8.0, 7.0, 6.5],
    'Bimestre3': [8.0, 7.0, 8.5, 7.5, 7.0],
    'Bimestre4': [7.0, 8.5, 8.0, 8.0, 8.5]
}
df_notas = pd.DataFrame(notas)
```

Desafio: Adicione pelo menos uma anotação destacando um insight importante nos seus gráficos.

## 🎨 Ferramentas de Visualização em Python

- **Matplotlib**: biblioteca fundamental para gráficos
- **Seaborn**: simplifica gráficos estatísticos
- **Plotly**: cria visualizações interativas
- **Bokeh**: gráficos interativos para web
- **Altair**: visualizações declarativas

## 🎯 Aplicação no Projeto Final
Suas visualizações avançadas podem incluir:
- Dashboards com métricas-chave para tomadores de decisão
- Análises de tendências temporais em dados de saneamento
- Mapas de calor mostrando correlações entre variáveis
- Gráficos comparativos entre regiões ou estados
- Visualizações interativas para apresentação de resultados