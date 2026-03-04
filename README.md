# 🦠 Predição de Zoonoses no Brasil com Machine Learning

Modelo preditivo para surtos de leptospirose e leishmaniose usando
dados epidemiológicos (SINAN), climáticos (INMET) e de saneamento (IBGE).

## Hipótese

Surtos de zoonoses são precedidos por padrões climáticos específicos
(chuvas intensas, temperaturas elevadas, alta umidade) combinados com
condições de saneamento precário, permitindo previsão antecipada de 1-3 meses.

## Fontes de Dados

| Fonte | Dados | Acesso |
|-------|-------|--------|
| SINAN/DATASUS | Casos confirmados de zoonoses | PySUS / FTP / Base dos Dados |
| INMET (BDMEP) | Precipitação, temperatura, umidade | portal.inmet.gov.br/dadoshistoricos |
| IBGE (SIDRA) | Saneamento, população | apisidra.ibge.gov.br |
| IBGE (Geociências) | Malha municipal | geobr (Python) |

## Metodologia

1. Agregação de casos por município × mês
2. Vinculação espacial de estações meteorológicas aos municípios (KDTree)
3. Feature engineering com lags temporais (1-3 meses)
4. Classificação de surto (acima do percentil 90)
5. Split temporal: Train (2010-2020) | Val (2021) | Test (2022-2023)
6. Comparação de modelos: LogReg, RF, GBM, HistGBM

## Stack

Python · PySUS · Pandas · Scikit-learn · GeoPandas · Folium · Streamlit

## Resultados

- Mapa de risco preditivo por município
- Feature importance (quais fatores mais influenciam surtos)
- Métricas: AUC-ROC, Average Precision, Recall

## Como Executar

```bash
pip install -r requirements.txt
# 1. Coleta (pode demorar — dados grandes)
jupyter notebook notebooks/01_coleta_sinan.ipynb
jupyter notebook notebooks/02_coleta_clima_saneamento.ipynb
# 2. Feature engineering
jupyter notebook notebooks/03_feature_engineering.ipynb
# 3. Modelagem
jupyter notebook notebooks/05_modelagem.ipynb
# 4. Dashboard
streamlit run app/streamlit_app.py
```

## Licença

MIT
