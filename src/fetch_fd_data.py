import os
import requests
import json
from dotenv import load_dotenv

# Carregar chave da API do .env
load_dotenv()
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")

# Endpoint da API - Portugal Primeira Liga (PPL)
url = "https://api.football-data.org/v4/competitions/PPL/matches"

headers = {"X-Auth-Token": API_KEY}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    os.makedirs("data", exist_ok=True)
    with open("data/ppl_matches.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("✔ Dados guardados em data/ppl_matches.json")
else:
    print(f"❌ Erro ao obter dados: {response.status_code}")
