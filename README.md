<h1 align="center">
  Predição de Zoonoses no Brasil
</h1>

<p align="center">
  <em>Modelo Preditivo para Surtos de Leptospirose e Leishmaniose com Machine Learning</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/GeoPandas-4479A1?logo=data&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" />
</p>

Análise preditiva e epidemiológica cruzando dados de saúde pública, anomalias climáticas e perfil de saneamento dos municípios brasileiros.

---

## Contexto Epidemiológico

Surtos de zoonoses como Leptospirose e Leishmaniose afetam severamente as regiões mais vulneráveis do Brasil todos os anos. Os surtos seguem um padrão sazonal atrelado a chuvas intensas ou secas severas, somados a gargalos de infraestrutura (saneamento básico precário, lixo urbano).

O objetivo deste projeto foi entender: é possível prever um surto epidêmico antes que ele sature o sistema de saúde? Como os dados climáticos do mês passado sinalizam o risco de contágio no próximo trimestre?

## A Hipótese e o Modelo

O projeto modelou o risco de surto (casos mensais acima do percentil 90 histórico do município) como um problema complexo de **Classificação Binária em Séries Temporais**.

Surtos de zoonoses são o resultado rastreável de uma cadeia de eventos. Através da aplicação de múltiplos lags temporais (defasagens de 1 a 3 meses) nas variáveis meteorológicas e auto-regressividade na série de contágio, o modelo atua como um sistema de alerta precoce. Validamos a abordagem com `Random Forest` e `HistGradientBoosting`, mantendo um rígido controle no split temporal para evitar data leakage.

O modelo final atingiu ROC-AUC de 0.87 no set de teste isolado (2022-2023).

## Dados

Todas as fontes são públicas, permitindo reprodutibilidade do estudo.

| Fonte | Dataset | Acesso |
|-------|---------|--------|
| SINAN/DATASUS | Casos confirmados de zoonoses (2010 a 2023) | PySUS (API pública) |
| INMET (BDMEP) | Temperatura horária, precipitação, umidade | Portal de Dados Históricos |
| IBGE/SIDRA | Municípios por tipo de esgotamento e população | API pública |
| IBGE | Malha municipal | geobr (Python) |

## Gráficos e Visualizações Analíticas

### Feature Importance do Modelo
![Importância Variáveis](docs/images/feature_importance.png)

### Regiões de Risco Extremo no Brasil
![Mapa de Risco](docs/images/risk_map.png)

### Avaliação (Curva ROC vs Falsos Positivos)
![Curva ROC](docs/images/roc_curve.png)

---

## Stack Tecnológica

| Tecnologia | Aplicação |
|-----------|-----------|
| Python | Linguagem principal |
| Scikit-learn | Treinamento de modelos ML e processamento |
| Pandas / GeoPandas | Engenharia de dados temporais e geolocalização |
| Jupyter | Exploração, EDA e documentação iterativa |
| Streamlit | Disponibilização do dashboard interativo de mapas |

---

## Como rodar

```bash
git clone https://github.com/mateusmmrs/predicao-zoonoses.git
cd predicao-zoonoses
pip install -r requirements.txt

# Ordem de execução de coletas e features
jupyter notebook notebooks/01_coleta_sinan.ipynb
jupyter notebook notebooks/02_coleta_clima_saneamento.ipynb
jupyter notebook notebooks/03_feature_engineering.ipynb

# Modelagem de Machine Learning
jupyter notebook notebooks/05_modelagem.ipynb
```

Nota: a etapa de feature engineering roda um cruzamento geométrico (via KDTree) em milhares de malhas do IBGE contra as estações do INMET e pode levar algum tempo localmente.

## Limitações

- Diagnóstico subnotificado no SINAN em regiões remotas do interior.
- As estações do INMET não cobrem 100% das áreas rurais (assumimos como proxy a estação mais próxima via distância euclidiana).
- Saneamento básico tratado como dado macro (por município), suprimindo nuances entre bairros.

---

**Mateus Martins** · Cientista de Dados · Inteligência Epidemiológica
