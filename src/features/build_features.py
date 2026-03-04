import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
import glob
import os

def build_feature_matrix():
    # Load SINAN (Leptospirose)
    sinan_files = glob.glob('data/raw/sinan/leptospirose_*.parquet')
    if not sinan_files:
        print("⚠️ Nenhum arquivo SINAN encontrado.")
        return
    
    df_sinan = pd.concat([pd.read_parquet(f) for f in sinan_files])
    df_conf = df_sinan[df_sinan['CLASSI_FIN'] == 1].copy()
    df_conf['dt_notific'] = pd.to_datetime(df_conf['DT_NOTIFIC'], errors='coerce')
    df_conf['ano_mes'] = df_conf['dt_notific'].dt.to_period('M')
    df_conf['code_muni'] = df_conf['ID_MUNICIP'].astype(str).str[:6]
    
    casos_muni_mes = df_conf.groupby(['code_muni', 'ano_mes']).size().reset_index(name='casos_leptospirose')
    
    # Save processed features
    os.makedirs('data/processed', exist_ok=True)
    casos_muni_mes.to_parquet('data/processed/features_baseline.parquet')
    print("✅ Feature matrix baseline criada")

if __name__ == "__main__":
    build_feature_matrix()
