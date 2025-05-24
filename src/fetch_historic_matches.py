import os
import requests
import json
from time import sleep

API_KEY = "5d88116019ca4b20b66267680c2bf13a"
headers = {"X-Auth-Token": API_KEY}

# Liga: PPL (Primeira Liga Portugal)
epocas = ["2020", "2021", "2022", "2023", "2024"]
all_matches = []

for epoca in epocas:
    url = f"https://api.football-data.org/v4/competitions/PPL/matches?season={epoca}"
    print(f"🕐 A buscar jogos da época {epoca}...")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dados = response.json()
        all_matches.extend(dados.get("matches", []))
        print(f"✔ {len(dados.get('matches', []))} jogos adicionados.")
    else:
        print(f"❌ Erro na época {epoca}: {response.status_code}")

    sleep(6)  # Evitar limite da API gratuita

# Guardar ficheiro
os.makedirs("data", exist_ok=True)
with open("data/ppl_all_matches.json", "w", encoding="utf-8") as f:
    json.dump(all_matches, f, indent=4)

print("✔ Todos os jogos guardados em data/ppl_all_matches.json")
