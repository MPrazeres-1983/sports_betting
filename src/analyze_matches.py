
import pandas as pd

# Carregar ficheiro CSV limpo
df = pd.read_csv("data/ppl_matches_clean.csv")

# Separar os golos em colunas distintas
df[["home_goals", "away_goals"]] = df["full_time_score"].str.split("-", expand=True).astype(int)

# Calcular total de golos por jogo
df["total_goals"] = df["home_goals"] + df["away_goals"]

# Determinar o vencedor
def vencedor(row):
    if row["home_goals"] > row["away_goals"]:
        return row["home_team"]
    elif row["home_goals"] < row["away_goals"]:
        return row["away_team"]
    else:
        return "Draw"

df["winner"] = df.apply(vencedor, axis=1)

# Estatísticas
media_golos = df["total_goals"].mean()
vitórias = df["winner"].value_counts()
jogos_mais_2_5 = df[df["total_goals"] > 2.5]

# Guardar estatísticas num CSV
stats_summary = pd.DataFrame({
    "media_golos_por_jogo": [media_golos],
    "jogos_totais": [len(df)],
    "jogos_mais_2_5_golos": [len(jogos_mais_2_5)],
    "empates": [(df["winner"] == "Draw").sum()]
})
stats_summary.to_csv("data/stats_summary.csv", index=False)

# Guardar vitórias por equipa
vitórias.to_csv("data/wins_by_team.csv")

print("✔ Análise concluída. Ficheiros gerados em /data:")
print("- stats_summary.csv")
print("- wins_by_team.csv")
