import pandas as pd

# Carregar dados
df = pd.read_csv("data/ppl_all_matches.csv")

# Garantir tipos corretos
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df[["home_goals", "away_goals"]] = df[["home_goals", "away_goals"]].astype(int)

# Calcular médias móveis
media_golos_movel = []
historico = {}
N = 3


def media(lista, tipo):
    if not lista:
        return 0.0
    return sum([x[tipo] for x in lista[-N:]]) / min(len(lista), N)


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

    historico.setdefault(home, []).append(
        {"gm": row["home_goals"], "gs": row["away_goals"]}
    )
    historico.setdefault(away, []).append(
        {"gm": row["away_goals"], "gs": row["home_goals"]}
    )

# Guardar CSV enriquecido
df_final = pd.DataFrame(media_golos_movel)
df_final.to_csv("data/ppl_all_enriched.csv", index=False)
print("✔ Ficheiro enriquecido criado: data/ppl_all_enriched.csv")
