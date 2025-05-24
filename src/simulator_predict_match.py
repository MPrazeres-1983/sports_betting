
import pandas as pd
from xgboost import XGBClassifier

# Carregar dataset e treinar modelo uma vez
df = pd.read_csv("data/ppl_all_enriched.csv")

# Calcular features derivadas
df["gm_diff"] = df["media_home_gm"] - df["media_away_gs"]
df["gs_diff"] = df["media_home_gs"] - df["media_away_gm"]
df["gm_combined"] = df["media_home_gm"] + df["media_away_gm"]

X = df[["media_home_gm", "media_home_gs", "media_away_gm", "media_away_gs", "gm_diff", "gs_diff", "gm_combined"]]
y = df["over_2_5"]

# Treinar modelo
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
model.fit(X, y)

print("\n🔮 Simulador de Previsão de Jogos (Over 2.5 golos) 🔮")
print("Insere as médias estimadas para cada equipa.\n")

while True:
    try:
        home_gm = float(input("⚽ Média de golos marcados pela equipa da casa: "))
        home_gs = float(input("🛡️ Média de golos sofridos pela equipa da casa: "))
        away_gm = float(input("⚽ Média de golos marcados pela equipa visitante: "))
        away_gs = float(input("🛡️ Média de golos sofridos pela equipa visitante: "))
    except ValueError:
        print("❌ Erro: Insere apenas valores numéricos.")
        continue

    # Calcular features derivadas
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
    print(f"\n🎯 Previsão: {resultado}")
    print(f"📊 Probabilidade de Over 2.5: {round(prob * 100, 2)}%\n")

    again = input("Queres simular outro jogo? (s/n): ").strip().lower()
    if again != "s":
        print("🔚 Obrigado por usares o simulador!")
        break
