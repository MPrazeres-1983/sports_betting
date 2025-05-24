
import pandas as pd
from xgboost import XGBClassifier

# Carregar o dataset e preparar as features
df = pd.read_csv("data/ppl_all_enriched.csv")

# Calcular médias por equipa como casa e visitante
medias = {}

equipas = sorted(set(df["home_team"]).union(set(df["away_team"])))

for equipa in equipas:
    casa = df[df["home_team"] == equipa]
    fora = df[df["away_team"] == equipa]

    total_jogos = len(casa) + len(fora)
    if total_jogos == 0:
        continue

    gm = pd.concat([casa["home_goals"], fora["away_goals"]]).mean()
    gs = pd.concat([casa["away_goals"], fora["home_goals"]]).mean()

    medias[equipa] = {
        "media_gm": round(gm, 2),
        "media_gs": round(gs, 2)
    }

# Calcular features derivadas para treino
df["gm_diff"] = df["media_home_gm"] - df["media_away_gs"]
df["gs_diff"] = df["media_home_gs"] - df["media_away_gm"]
df["gm_combined"] = df["media_home_gm"] + df["media_away_gm"]

X = df[["media_home_gm", "media_home_gs", "media_away_gm", "media_away_gs", "gm_diff", "gs_diff", "gm_combined"]]
y = df["over_2_5"]

# Treinar modelo
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
model.fit(X, y)

# Início da interação
print("\n🔮 Simulador de Previsão por Equipas (Over 2.5 golos) 🔮\n")

while True:
    print("Lista de Equipas Disponíveis:")
    for idx, equipa in enumerate(equipas):
        print(f"{idx + 1}. {equipa}")

    try:
        home_idx = int(input("\n🏠 Escolhe o número da equipa da CASA: ")) - 1
        away_idx = int(input("🛫 Escolhe o número da equipa VISITANTE: ")) - 1
        home_team = equipas[home_idx]
        away_team = equipas[away_idx]
    except (ValueError, IndexError):
        print("❌ Escolha inválida. Tenta novamente.\n")
        continue

    if home_team == away_team:
        print("❌ As equipas não podem ser iguais.\n")
        continue

    # Buscar médias
    home_gm = medias[home_team]["media_gm"]
    home_gs = medias[home_team]["media_gs"]
    away_gm = medias[away_team]["media_gm"]
    away_gs = medias[away_team]["media_gs"]

    # Calcular features
    input_data = {
        "media_home_gm": home_gm,
        "media_home_gs": home_gs,
        "media_away_gm": away_gm,
        "media_away_gs": away_gs,
        "gm_diff": home_gm - away_gs,
        "gs_diff": home_gs - away_gm,
        "gm_combined": home_gm + away_gm
    }

    df_input = pd.DataFrame([input_data])
    pred = model.predict(df_input)[0]
    prob = model.predict_proba(df_input)[0][1]

    resultado = "🔥 Over 2.5 golos" if pred == 1 else "🧊 Under 2.5 golos"
    print(f"\n🎯 Previsão para {home_team} vs {away_team}: {resultado}")
    print(f"📊 Probabilidade de Over 2.5: {round(prob * 100, 2)}%\n")

    again = input("Simular outro jogo? (s/n): ").strip().lower()
    if again != "s":
        print("🔚 Obrigado por usares o simulador!")
        break
