import pandas as pd
import json

# Ler ficheiro JSON
with open("data/ppl_matches.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Extrair lista de jogos
matches = raw_data.get("matches", [])

# Processar para lista de dicionários simples
rows = []
for match in matches:
    row = {
        "date": match.get("utcDate", "")[:10],
        "home_team": match["homeTeam"]["name"],
        "away_team": match["awayTeam"]["name"],
        "full_time_score": f'{match["score"]["fullTime"]["home"]}-{match["score"]["fullTime"]["away"]}',
        "status": match.get("status", ""),
    }
    rows.append(row)

# Criar DataFrame
df = pd.DataFrame(rows)

# Guardar em CSV
df.to_csv("data/ppl_matches_clean.csv", index=False)
print("✔ Ficheiro CSV criado: data/ppl_matches_clean.csv")
