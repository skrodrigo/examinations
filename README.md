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

## 🔧 Instalação e Execução

1. Certifique-se de ter Python 3.x instalado em seu sistema

2. Instale as bibliotecas necessárias usando pip:
```bash
pip install streamlit pandas plotly
```

3. Para executar a aplicação, navegue até a pasta do projeto e use um dos comandos:
```bash
# Se estiver na pasta raiz do projeto:
streamlit run src/app.py

# Ou especifique o caminho completo:
streamlit run [caminho_completo]/src/app.py
```

4. Após executar o comando, o Streamlit abrirá automaticamente seu navegador padrão com a aplicação

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

## 💡 Dicas de Uso

- A aplicação carregará automaticamente após executar o comando streamlit
- Aguarde alguns segundos para que todos os gráficos sejam carregados
- Use a barra lateral para navegar entre diferentes visualizações
- Os gráficos são interativos - você pode passar o mouse sobre eles para ver mais detalhes

## ❗ Requisitos do Sistema

- Python 3.x
- Navegador web moderno
- Conexão com a internet (para carregar algumas dependências do Plotly)

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

Desenvolvido com ❤️ por Rodrigo e Lívia para Lívia