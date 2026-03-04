from pysus.ftp.databases.sinan import SINAN
import os
import pandas as pd

def extract_leptospirose(years=range(2010, 2024)):
    sinan = SINAN().load()
    output_dir = 'data/raw/sinan'
    os.makedirs(output_dir, exist_ok=True)
    
    for year in years:
        try:
            files = sinan.get_files('LEPT', year)
            df = sinan.download(files).to_dataframe()
            df.to_parquet(f'{output_dir}/leptospirose_{year}.parquet')
            print(f"  ✅ {year}: {len(df)} registros")
        except Exception as e:
            print(f"  ❌ {year}: {e}")

if __name__ == "__main__":
    extract_leptospirose()
