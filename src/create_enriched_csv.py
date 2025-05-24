import pandas as pd

# Carregar os dados
df = pd.read_csv("data/ppl_matches_clean.csv")

# Separar os golos
df[["home_goals", "away_goals"]] = (
    df["full_time_score"].str.split("-", expand=True).astype(int)
)

# Ordenar por data
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Criar estruturas auxiliares
media_golos_movel = []
historico = {}
N = 3  # número de jogos anteriores a considerar


# Função auxiliar
def media(lista, tipo):
    if not lista:
        return 0.0
    return sum([x[tipo] for x in lista[-N:]]) / min(len(lista), N)


# Calcular médias por jogo
for _, row in df.iterrows():
    home = row["home_team"]
    away = row["away_team"]

    hist_home = historico.get(home, [])
    hist_away = historico.get(away, [])

    media_home_gm = media(hist_home, "gm")
    media_home_gs = media(hist_home, "gs")
    media_away_gm = media(hist_away, "gm")
    media_away_gs = media(hist_away, "gs")

    media_golos_movel.append(
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "home_team": home,
            "away_team": away,
            "home_goals": row["home_goals"],
            "away_goals": row["away_goals"],
            "media_home_gm": media_home_gm,
            "media_home_gs": media_home_gs,
            "media_away_gm": media_away_gm,
            "media_away_gs": media_away_gs,
            "over_2_5": int((row["home_goals"] + row["away_goals"]) > 2.5),
        }
    )

    # Atualizar histórico
    historico.setdefault(home, []).append(
        {"gm": row["home_goals"], "gs": row["away_goals"]}
    )
    historico.setdefault(away, []).append(
        {"gm": row["away_goals"], "gs": row["home_goals"]}
    )

# Criar DataFrame e guardar
df_final = pd.DataFrame(media_golos_movel)
df_final.to_csv("data/ppl_matches_enriched.csv", index=False)

print("✔ Ficheiro enriquecido criado: data/ppl_matches_enriched.csv")
