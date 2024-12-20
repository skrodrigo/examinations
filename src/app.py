import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Configurações globais de estilo
FONT_STYLE = {
    'family': 'Times New Roman',
    'size': 14,
    'color': 'black'
}

# Configuração global para todos os gráficos Plotly
import plotly.io as pio
pio.templates["custom"] = pio.templates["plotly_white"]
pio.templates["custom"].layout.update(
    font=FONT_STYLE,
    title_font=FONT_STYLE,
    xaxis_title_font=FONT_STYLE,
    yaxis_title_font=FONT_STYLE
)
pio.templates.default = "custom"

# Carregando os dados JSON
with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

# st.title('Análise')

# Definindo uma paleta de cores em tons pastéis
cores = [

  '#CED4DA', 
  '#ADB5BD', 
  '#6C757D', 
  '#495057', 
  '#343A40', 
  '#212529'  
]

# 1. Tabela de Antibióticos
# st.header('Antibióticos Testados')
antibiotics_data = {
    'Antibiótico': data['resumo_exames']['antibioticos_testados'],
    'MCG/UN': [
        '30mcg', '10mcg', '30mcg', '30mcg', '5mcg', 
        '-', '2mcg', '30mcg', '10mcg', '300mcg',
        '10mcg', '30mcg', '30mcg', '30mcg', '30mcg',
        '10mcg', '10UI', '25mcg', '-', '300mcg', '10mcg'
    ]
}
antibiotics_df = pd.DataFrame(antibiotics_data)
# Adiciona coluna de índice começando em 1
antibiotics_df.index = range(1, len(antibiotics_df) + 1)

# Estilizar a tabela com cores
def highlight_columns(x):
    return pd.DataFrame({
        'background-color': '#CED4DA',
        'color': 'black',
        'font-family': 'Times New Roman',
        'font-size': '14px'
    }, index=x.index, columns=x.columns)

# Aplicar o estilo e mostrar a tabela
styled_df = antibiotics_df.style.set_table_styles([
    {'selector': 'th', 'props': [
        ('background-color', '#CED4DA'),
        ('color', 'black'),
        ('font-family', 'Times New Roman'),
        ('font-size', '16px'),
        ('border', 'none'),
        ('padding', '8px')
    ]},
    {'selector': 'td', 'props': [
        ('color', 'black'),
        ('font-family', 'Times New Roman'),
        ('font-size', '14px'),
        ('border', 'none'),
        ('padding', '8px')
    ]},
    {'selector': 'table', 'props': [
        ('border-collapse', 'collapse'),
        ('border', 'none'),
        ('margin', '0px')
    ]}
])
st.table(styled_df)

# Tabelas de Antibióticos Resistentes e Sensíveis
# st.subheader('Antibióticos Resistentes')

# Para os Antibióticos Resistentes
resistant_data = {
    'Antibiótico': [
        'Ampicilina 10mcg',
        'Cefalexina 30mcg',
        'Clindamicina 2mcg',
        'Tetraciclina 30mcg',
        'Ceftriaxona 30mcg',
        'Ciprofloxacino 5mcg',
        'Penicilina G',
        'Sulfazotrim 25mcg',
        'Aztreonam',
        'Sulfanamidas 300mcg',
        'Tobramicina 10mcg',
        'Norfloxacina 10mcg'
    ],
    'Quantidade': [2, 1, 5, 1, 1, 1, 1, 1, 1, 2, 1, 1]
}

resistant_df = pd.DataFrame(resistant_data)
resistant_df = resistant_df.sort_values('Quantidade', ascending=True)

# Calcular percentuais
total_resistant = resistant_df['Quantidade'].sum()
resistant_df['Percentual'] = (resistant_df['Quantidade'] / total_resistant * 100).round(2)

# Criar gráfico de barras horizontal para resistentes
fig_resistant = px.bar(resistant_df,
                      y='Antibiótico',
                      x='Percentual',
                      #title = 'Resistência do Patôgeno <i>Escherichia coli</i> aos Antibióticos',
                      color_discrete_sequence=['#CED4DA'],
                      orientation='h')

fig_resistant.update_layout(
    height=600,
    showlegend=False,
    font=FONT_STYLE,
    xaxis=dict(
        title='Percentual (%)',
        gridcolor='lightgray',
        range=[0, max(resistant_df['Percentual']) + 5],
        title_font=FONT_STYLE,
        tickfont=FONT_STYLE
    ),
    yaxis=dict(
        title='',
        tickfont=FONT_STYLE
    )
)

fig_resistant.update_traces(
    texttemplate='%{x:.1f}%',
    textposition='outside',
    textfont=FONT_STYLE
)

st.plotly_chart(fig_resistant)

# Gráfico de Antibióticos Sensíveis
#st.subheader('Antibióticos Sensíveis')

sensitive_data = {
    'Antibiótico': [
        "Amicacina",
        "Cefalexina",
        "Cefoxitina",
        "Ciprofloxacina",
        "Amoxicilina + Ac. Clavulanico",
        "Cloranfenicol",
        "Gentamicina",
        "Nitrofurantoína",
        "Norfloxacina",
        "Cefuroxima",
        "Imipenem",
        "Tetraciclina",
        "Ampicilina",
        "Ceftriaxona",
        "Sulfazotrim",
        "Tobramicina",
        "Penicilina G",
        "Sulfonamidas",
        "Aztreonam"
    ],
    'Quantidade': [  
        5,  # Amicacina
        4,  # Cefalexina
        4,  # Cefoxitina
        4,  # Ciprofloxacina
        2,  # Amoxicilina + Ac. Clavulanico
        4,  # Cloranfenicol
        4,  # Gentamicina
        4,  # Nitrofurantoína
        3,  # Norfloxacina
        1,  # Cefuroxima
        1,  # Imipenem
        3,  # Tetraciclina
        3,  # Ampicilina
        3,  # Ceftriaxona
        1,  # Sulfazotrim
        1,  # Tobramicina
        1,  # Penicilina G
        1,  # Sulfonamidas
        1,  # Aztreonam
    ]
}

sensitive_df = pd.DataFrame(sensitive_data)

# Ordenar o DataFrame por quantidade em ordem decrescente
sensitive_df = sensitive_df.sort_values('Quantidade', ascending=True)

# Calcular percentuais
total_sensitive = sensitive_df['Quantidade'].sum()
sensitive_df['Percentual'] = (sensitive_df['Quantidade'] / total_sensitive * 100).round(2)

# Criar gráfico de barras horizontal para sensíveis
fig_sensitive = px.bar(sensitive_df,
                      y='Antibiótico',
                      x='Percentual',
                     # title = 'Sensibilidade do Patôgeno <i>Escherichia coli</i> aos Antibióticos',
                      color_discrete_sequence=['#CED4DA'],
                      orientation='h')

fig_sensitive.update_layout(
    height=600,
    showlegend=False,
    font=FONT_STYLE,
    xaxis=dict(
        title='Percentual (%)',
        gridcolor='lightgray',
        range=[0, max(sensitive_df['Percentual']) + 5],
        title_font=FONT_STYLE,
        tickfont=FONT_STYLE
    ),
    yaxis=dict(
        title='',
        tickfont=FONT_STYLE
    )
)

fig_sensitive.update_traces(
    texttemplate='%{x:.1f}%',
    textposition='outside',
    textfont=FONT_STYLE
)

st.plotly_chart(fig_sensitive)

# 2. Gráfico de Uroculturas Positivas
#st.header('Análise de Uroculturas Positivas')
urine_data = data['resumo_exames']['resumo_urina']

# Criar DataFrame para uroculturas positivas com dados atualizados
positive_data = {
    'Parâmetro': [
        'Nitrito (Positivo)',
        'Nitrito (Negativo)',
        'Leucócitos (Positivos)',
        'Leucócitos (Negativos)',
        'Aspecto (Turvo)',
        'Aspecto (Ligeiramente Turvo)',
        'Bactérias (Incontáveis 5+)',
        'Bactérias (Numerosas 4+)',
        'Bactérias (Numerosas 3+)',
        'Bactérias (Aumentadas 3+)',
    ],
    'Percentual': [
        urine_data['nitrito']['positivo'],
        20,  # Nitrito Negativo 20%
        urine_data['leucocitos']['numerosos'],
        40,  # Leucócitos Negativos 40%
        urine_data['aspecto']['turvo'],
        urine_data['aspecto']['ligeiramente_turvo'],
        urine_data['bacterias']['incontaveis_5_mais'],
        urine_data['bacterias']['numerosas_4_mais'],
        urine_data['bacterias']['numerosas_3_mais'],
        urine_data['bacterias']['aumentadas_3_mais'],
    ]
}
positive_df = pd.DataFrame(positive_data)

fig_positive = px.bar(positive_df, y='Parâmetro', x='Percentual',
                     #title='Parâmetros em Uroculturas Positivas',
                     labels={'Percentual': 'Percentual (%)'},
                     color_discrete_sequence=['#CED4DA'],  # Rosa pastel
                     orientation='h')

fig_positive.update_layout(
    showlegend=False,
    height=600,
    font=FONT_STYLE,
    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=10,
        gridcolor='lightgray',
        range=[0, 100],
        title_font=FONT_STYLE,
        tickfont=FONT_STYLE
    ),
    yaxis=dict(
        tickfont=FONT_STYLE
    ),
    hoverlabel=dict(
        bgcolor="white",
        font=FONT_STYLE
    )
)

fig_positive.update_traces(
    texttemplate='%{x}%',
    textposition='outside',
    textfont=FONT_STYLE
)

st.plotly_chart(fig_positive)

# 3. Gráfico de Parâmetros Físicos

#st.header('Parâmetros Físicos')
physical_params = data['resumo_exames']['analise_parametros']

# Calcular porcentagens
total_exames = 53

# Para cor
color_df = pd.DataFrame([{
    'Parâmetro': k.replace('amarelo_claro', 'Amarelo Claro').replace('palha', 'Amarelo Palha').replace('citrino', 'Amarelo Citrino').replace('escuro', 'Amarelo Escuro').replace('_', ' ').title(),
    'Quantidade': v,
    'Percentual': round((v/total_exames)*100, 2)  # Arredondar para 2 casas decimais
} for k, v in physical_params['cor'].items()])

# Para densidade
density_df = pd.DataFrame([{
    'Parâmetro': f"Densidade {k}",
    'Quantidade': v,
    'Percentual': round((v/sum(physical_params['densidade'].values()))*100, 2)  # Calcular percentual do total de densidades
} for k, v in physical_params['densidade'].items()])

# Para aspecto
appearance_df = pd.DataFrame([{
    'Parâmetro': f"Aspecto {k.replace('ligeiramente_turvo', 'Ligeiramente Turvo').replace('turvo', 'Turvo').replace('limpido', 'Límpido').replace('_', ' ').title()}",
    'Quantidade': v,
    'Percentual': round((v/total_exames)*100, 2)  # Arredondar para 2 casas decimais
} for k, v in physical_params['aspecto'].items()])

# Concatenar todos os DataFrames para exibição
final_df = pd.concat([color_df, density_df, appearance_df])

# Gráfico de Parâmetros Físicos
fig_physical = px.bar(final_df, 
                      y='Parâmetro', 
                      x='Percentual', 
                     # title='Análise dos Parâmetros Físicos das Uroculturas',
                      labels={'Percentual': 'Percentual (%)'},
                      color_discrete_sequence=['#CED4DA'],  # Rosa pastel
                      orientation='h')

fig_physical.update_layout(
    showlegend=False,
    height=600,
    font=FONT_STYLE,
    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=10,
        gridcolor='lightgray',
        range=[0, 80],
        title_font=FONT_STYLE,
        tickfont=FONT_STYLE
    ),
    yaxis=dict(
        tickfont=FONT_STYLE
    ),
    hoverlabel=dict(
        bgcolor="white",
        font=FONT_STYLE
    )
)

fig_physical.update_traces(
    texttemplate='%{x:.1f}%',  # Formatando para mostrar apenas 2 casas decimais
    textposition='outside',
    textfont=FONT_STYLE
)

st.plotly_chart(fig_physical)

# 4. Gráfico de Parâmetros Químicos
#st.header('Parâmetros Químicos')
chemical_data = {
    'Parâmetro': [
        'pH 5.0',
        'pH 6.0',
        'pH 6.5',
        'pH 7.0',
        'pH 7.5',
        'Proteína (Positivo)',
        'Proteína (Negativo)',
        'Glicose (Positivo)',
        'Glicose (Negativo)',
        'Urobilinogênio (Normal)',
        'Bilirrubina (Negativo)',
        'Corpos Cetônicos (Positivo)',
        'Corpos Cetônicos (Negativo)',
        'Cristais (Ausentes)',
        'Filamento de Muco (Positivo)',
        'Filamento de Muco (Negativo)'
    ],
    'Quantidade': [
        physical_params['ph']['ph5'],
        physical_params['ph']['ph6'],
        physical_params['ph']['ph6.5'],
        physical_params['ph']['ph7'],
        physical_params['ph']['ph7.5'],
        1,
        physical_params['proteina']['negativo'],
        3,
        50,  # Glicose negativa (53 - 3 positivos)
        53,
        53,
        4,
        49,  # Corpos cetônicos negativos (53 - 4 positivos)
        53,
        4,
        49   # Filamento de muco negativos (53 - 4 positivos)
    ]
}
chemical_df = pd.DataFrame(chemical_data)

# Calcular percentuais
chemical_df['Percentual'] = (chemical_df['Quantidade'] / total_exames * 100).round(2)

fig_chemical = px.bar(chemical_df, y='Parâmetro', x='Percentual',
                     #title='Parâmetros Químicos da Urina',
                     labels={'Percentual': 'Percentual (%)'},
                     color='Parâmetro',
                     color_discrete_sequence=['#CED4DA'],
                     orientation='h')

fig_chemical.update_layout(
    showlegend=False,
    height=600,
    font=FONT_STYLE,
    xaxis=dict(
        range=[0, 116],
        title_font=FONT_STYLE,
        tickfont=FONT_STYLE
    ),
    yaxis=dict(
        tickfont=FONT_STYLE
    ),

)

# Adiciona rótulos de valor em cada barra
fig_chemical.update_traces(
    texttemplate='%{x:.1f}%',
    textposition='outside',
    textfont=FONT_STYLE
)

st.plotly_chart(fig_chemical)

# 5. Gráfico de Parâmetros Microbiológicos (convertido para pizza)
#st.header('Parâmetros Microbiológicos')
micro_data = {
    'Parâmetro': [
        'Hemácias (Raras)',
        'Leucócitos (Raros)',
        'Bactérias (Raras)',
        'Células Epiteliais (Raras)'
    ],
    'Quantidade': [2, 
                  physical_params['leucocitos']['raros'],
                  21,
                  physical_params['celulas_epiteliais']['raras']]
}
micro_df = pd.DataFrame(micro_data)

# Calcular percentuais
micro_df['Percentual'] = (micro_df['Quantidade'] / total_exames * 100).round(2)

fig_micro = px.pie(micro_df, 
                  values='Percentual',
                  names='Parâmetro',
                 # title='Parâmetros Microbiológicos da Urina',
                  color_discrete_sequence=cores)

fig_micro.update_layout(
    showlegend=True,
    font=FONT_STYLE,
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="right",
        x=1.6,
        font=dict(size=18)
    ),
    height=600
)

st.plotly_chart(fig_micro)