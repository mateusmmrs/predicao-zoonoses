import requests
import pandas as pd
import os

def extract_saneamento():
    output_dir = 'data/raw/ibge'
    os.makedirs(output_dir, exist_ok=True)
    
    # Tabela 3218: Domicílios por esgotamento sanitário
    url_san = "https://apisidra.ibge.gov.br/values/t/3218/n6/all/v/all/p/last%201/c61/allxt"
    try:
        resp = requests.get(url_san, timeout=300)
        data_san = resp.json()
        df_saneamento = pd.DataFrame(data_san[1:])
        df_saneamento.to_csv(f'{output_dir}/saneamento_municipios.csv', index=False)
        print("✅ Saneamento extraído")
    except Exception as e:
        print(f"❌ Erro saneamento: {e}")

def extract_populacao():
    output_dir = 'data/raw/ibge'
    os.makedirs(output_dir, exist_ok=True)
    
    url_pop = "https://apisidra.ibge.gov.br/values/t/6579/n6/all/v/all/p/last%201"
    try:
        resp = requests.get(url_pop)
        data_pop = resp.json()
        df_pop = pd.DataFrame(data_pop[1:])
        df_pop.to_csv(f'{output_dir}/populacao_municipios.csv', index=False)
        print("✅ População extraída")
    except Exception as e:
        print(f"❌ Erro população: {e}")

if __name__ == "__main__":
    extract_saneamento()
    extract_populacao()
