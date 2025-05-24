
import json
import pandas as pd

# Carregar ficheiro JSON com todos os jogos
with open("data/ppl_all_matches.json", "r", encoding="utf-8") as f:
    matches = json.load(f)

# Preparar dados formatados
rows = []
for match in matches:
    if match["status"] == "FINISHED":
        rows.append({
            "date": match["utcDate"][:10],
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "home_goals": match["score"]["fullTime"]["home"],
            "away_goals": match["score"]["fullTime"]["away"]
        })

# Criar DataFrame
df = pd.DataFrame(rows)

# Guardar CSV
df.to_csv("data/ppl_all_matches.csv", index=False)
print("✔ CSV criado com sucesso: data/ppl_all_matches.csv")
