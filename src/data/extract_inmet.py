import requests
import zipfile
import os
from io import BytesIO

def download_historical_inmet(years=range(2010, 2024)):
    output_dir = 'data/raw/inmet'
    os.makedirs(output_dir, exist_ok=True)

    for year in years:
        url = f"https://portal.inmet.gov.br/uploads/dadoshistoricos/{year}.zip"
        print(f"Baixando {year}...")

        try:
            resp = requests.get(url, timeout=120)
            if resp.status_code == 200:
                zip_path = f'{output_dir}/{year}.zip'
                with open(zip_path, 'wb') as f:
                    f.write(resp.content)

                with zipfile.ZipFile(zip_path, 'r') as z:
                    z.extractall(f'{output_dir}/{year}/')
                print(f"  ✅ {year}")
            else:
                print(f"  ❌ {year}: HTTP {resp.status_code}")
        except Exception as e:
            print(f"  ❌ {year}: {e}")

if __name__ == "__main__":
    download_historical_inmet()
