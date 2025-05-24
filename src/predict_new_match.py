
import pandas as pd
import joblib
from xgboost import XGBClassifier

# Dados manuais para previsão (exemplo)
novo_jogo = {
    "media_home_gm": 1.6,   # média de golos marcados pela casa
    "media_home_gs": 1.2,   # média de golos sofridos pela casa
    "media_away_gm": 1.4,   # média de golos marcados pela visitante
    "media_away_gs": 1.1    # média de golos sofridos pela visitante
}

# Calcular features derivadas
novo_jogo["gm_diff"] = novo_jogo["media_home_gm"] - novo_jogo["media_away_gs"]
novo_jogo["gs_diff"] = novo_jogo["media_home_gs"] - novo_jogo["media_away_gm"]
novo_jogo["gm_combined"] = novo_jogo["media_home_gm"] + novo_jogo["media_away_gm"]

# Transformar em DataFrame
df_input = pd.DataFrame([novo_jogo])

# Treinar novamente o modelo (podes guardar num .pkl no futuro)
df = pd.read_csv("data/ppl_all_enriched.csv")
df["gm_diff"] = df["media_home_gm"] - df["media_away_gs"]
df["gs_diff"] = df["media_home_gs"] - df["media_away_gm"]
df["gm_combined"] = df["media_home_gm"] + df["media_away_gm"]

X = df[["media_home_gm", "media_home_gs", "media_away_gm", "media_away_gs", "gm_diff", "gs_diff", "gm_combined"]]
y = df["over_2_5"]

model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
model.fit(X, y)

# Prever novo jogo
pred = model.predict(df_input)[0]
prob = model.predict_proba(df_input)[0][1]

resultado = "Over 2.5 golos" if pred == 1 else "Under 2.5 golos"
print(f"🔮 Previsão: {resultado}")
print(f"📊 Probabilidade de Over 2.5: {round(prob * 100, 2)}%")
