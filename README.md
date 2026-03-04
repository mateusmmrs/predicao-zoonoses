# 🦠 Predição de Zoonoses no Brasil com Machine Learning

> **Análise Preditiva e Mapeamento de Risco para Leptospirose e Leishmaniose**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-2.0-150458.svg)
![GeoPandas](https://img.shields.io/badge/GeoPandas-Spatial-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)

---

## 📖 Visão Geral do Projeto

Este projeto consiste em um sistema completo de inteligência de dados voltado para a saúde pública, capaz de prever surtos de zoonoses (Leptospirose, Leishmaniose) com **1 a 3 meses de antecedência**. 

Através do cruzamento de dados epidemiológicos, anomalias climáticas e perfis de saneamento básico dos municípios, o modelo atua como um sistema de alerta precoce, auxiliando na alocação de recursos médicos e campanhas de prevenção.

### 💡 A Hipótese Central
**Surtos de zoonoses são o resultado rastreável de uma cadeia de eventos.**
O modelo foi construído sob a premissa de que padrões climáticos extremos (chuvas intensas, secas severas) atuam como catalisadores em municípios com certas vulnerabilidades de infraestrutura (saneamento precário, alta densidade), criando um "delay" previsível até o início do surto epidêmico.

---

## 📊 Arquitetura de Dados e Pipeline

O projeto consome exclusivamente dados públicos e abertos do Governo Federal, estruturados no seguinte pipeline:

| Fonte de Dados | Propósito no Modelo | Variáveis Coletadas |
|----------------|---------------------|---------------------|
| **SINAN / DATASUS** | **Target (Alvo)** | Registros individuais confirmados de Leptospirose e Leishmaniose (2010 a 2023). Agregado mensalmente por município. |
| **INMET** | **Sinais Ambientais** | Dados de centenas de estações meteorológicas (Temperatura, Precipitação e Umidade) com *Lags Temporais*. |
| **IBGE (PNSB / Censo)** | **Risco Estrutural** | Índices de esgotamento sanitário, acesso a água tratada e coleta de lixo. |
| **Geociências (IBGE)**| **Inteligência Espacial** | Malha municipal para match geográfico (via KDTree) e visualização de mapas. |

### Processamento de Features (Feature Engineering)
A inteligência do modelo reside nas variáveis defasadas (lags):
- **Lags Climáticos (1, 2, 3 meses):** O volume de chuvas de hoje impacta os casos de leptospirose daqui a 60 dias.
- **Sazonalidade Cíclica:** Transformações Trigonométricas (Seno/Cosseno) dos meses do ano.
- **Auto-regressividade:** Casos registrados no mês anterior como preditor forte de tendência.
- **Incidência Normalizada:** Conversão de valores absolutos para taxa por 100k habitantes.

---

## 🤖 Modelagem Preditiva e Resultados

O problema foi modelado como uma tarefa de **Classificação Binária** para detecção de anomalias temporais (Surtos), onde a classe "1" representa casos acima do percentil 90 histórico do município.

Devido à natureza temporal, utilizamos validação cruzada **TimeSeriesSplit** e evitamos categoricamente splits aleatórios (data leakage). Avaliamos múltiplos algoritmos: `Logistic Regression`, `Random Forest`, `Gradient Boosting` e `HistGradientBoosting`.

### 🎯 Feature Importance (Influência das Variáveis)
Abaixo, a visualização dos fatores que mais determinam a chance de um surto ocorrer, extraídos do melhor modelo (Ensemble Baseado em Árvores):

![Feature Importance](docs/images/feature_importance.png)
*(Os lags climáticos e o histórico recente da doença dominam a importância preditiva).*

### 📈 Desempenho do Modelo (ROC e Precision-Recall)
O modelo atinge excelentes taxas de recall na identificação precoce do risco, otimizando o trade-off entre falsos positivos e a identificação de áreas necessitadas.

![Curva ROC](docs/images/roc_curve.png)
> **Métricas (Test Set - 2022/2023):**
> - **AUC-ROC:** 0.87
> - **Average Precision (PR-AUC):** 0.74

---

## 🗺️ Mapa de Risco Preditivo (Output)

O produto final do modelo é um **Mapa de Calor de Risco Preditivo**. Através de visualizações geoespaciais e da aplicação web interativa em Streamlit, gestores de saúde visualizam a probabilidade de surtos para o próximo trimestre.

![Mapa de Risco Brasil](docs/images/risk_map.png)

---

## 💻 Reproduzindo o Projeto

A codebase está estruturada em formato modular.

### Pré-requisitos
```bash
git clone https://github.com/mateusmmrs/predicao-zoonoses.git
cd predicao-zoonoses
pip install -r requirements.txt
```

### Ordem de Execução
Para reproduzir a pesquisa e o modelo, execute os Notebooks sequencialmente:

1. **`01_coleta_sinan.ipynb`**: Consome a API do PySUS para o DATASUS.
2. **`02_coleta_clima_saneamento.ipynb`**: Raspagem via requests do INMET e via SIDRA do IBGE.
3. **`03_feature_engineering.ipynb`**: Construção da grande matriz de variáveis defasadas.
4. **`04_eda_zoonoses.ipynb`**: Análise Exploratória e estatística espacial.
5. **`05_modelagem.ipynb`**: Treinamento, validação temporal cruzada e deploy do artefato `.pkl`.
6. **`06_avaliacao_mapas.ipynb`**: Geração geoespacial.
7. **`app/streamlit_app.py`**: *(Opcional)* Rode com `streamlit run app/streamlit_app.py` para abrir o dashboard final.

---

> Desenvolvido por Mateus — Portfólio de Ciência de Dados
