# Análise de Exames Laboratoriais

## 📋 Sobre o Projeto
Este projeto é uma aplicação web desenvolvida com Streamlit para análise e visualização de dados de exames laboratoriais, com foco em uroculturas e antibiogramas. A aplicação fornece visualizações interativas e análises detalhadas de diversos parâmetros relacionados a exames de urina.

## 🚀 Funcionalidades

- Visualização de antibióticos testados e suas concentrações
- Análise de resistência e sensibilidade bacteriana
- Gráficos detalhados de parâmetros físicos, químicos e microbiológicos
- Análise de uroculturas positivas
- Visualização de distribuição de resultados por diferentes parâmetros

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Streamlit
- Pandas
- Plotly Express
- JSON

## 📦 Estrutura do Projeto
.
├── app.py # Aplicação principal Streamlit
├── data.json # Arquivo de dados
└── README.md # Documentação


## 🔧 Instalação

1. Clone o repositório:
git clone https://github.com/skrodrigo/examinations-with-python

2. Instale as dependências:

pip install -r requirements.txt

3. Execute a aplicação:

streamlit run app.py


## 📊 Visualizações Disponíveis

### 1. Antibióticos
- Tabela completa de antibióticos testados
- Gráficos de resistência bacteriana
- Gráficos de sensibilidade bacteriana

### 2. Análise de Uroculturas
- Parâmetros em uroculturas positivas
- Distribuição de resultados

### 3. Parâmetros Físicos
- Cor
- Densidade
- Aspecto

### 4. Parâmetros Químicos
- pH
- Proteínas
- Glicose
- Outros indicadores químicos

### 5. Parâmetros Microbiológicos
- Hemácias
- Leucócitos
- Bactérias
- Células epiteliais

## 📈 Dados

Os dados são armazenados em formato JSON e incluem:
- Total de 53 exames analisados
- Informações detalhadas sobre uroculturas positivas e negativas
- Dados completos de antibiograma
- Parâmetros físico-químicos das amostras

## 🎨 Estilização

A aplicação utiliza uma paleta de cores em tons pastéis, com ênfase em:
- Rosa claro (#FFB3BA)
- Tons complementares para melhor visualização dos gráficos

---

Desenvolvido com ❤️ por Rodrigo e Lívia par Lívia



