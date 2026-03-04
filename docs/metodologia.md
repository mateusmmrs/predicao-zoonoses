# Metodologia de Predição de Zoonoses

## 1. Coleta de Dados
As fontes primárias são o SINAN (epidemiológico), INMET (climático) e IBGE (geográfico e sanitário).

## 2. Processamento Espacial
Os municípios são vinculados às estações meteorológicas mais próximas utilizando um algoritmo de KDTree (vizinho mais próximo).

## 3. Engenharia de Variáveis
- **Atributos de Tempo**: Mês e ano, representações cíclicas (seno/cosseno).
- **Lags**: Atrasos de 1 a 3 meses para precipitação e temperatura, capturando o tempo de incubação e reprodução de vetores.
- **Variável Alvo**: Classificação binária de surto baseada no percentil 90 de casos históricos.

## 4. Modelagem
Uso de modelos de conjunto (Random Forest, Gradient Boosting) com validação cruzada temporal para garantir a robustez contra vazamento de dados futuros.
