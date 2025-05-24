
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carregar o dataset
df = pd.read_csv("data/ppl_all_enriched.csv")

# Features (incluindo diferenças) e target
df["gm_diff"] = df["media_home_gm"] - df["media_away_gs"]
df["gs_diff"] = df["media_home_gs"] - df["media_away_gm"]
df["gm_combined"] = df["media_home_gm"] + df["media_away_gm"]

X = df[["media_home_gm", "media_home_gs", "media_away_gm", "media_away_gs", "gm_diff", "gs_diff", "gm_combined"]]
y = df["over_2_5"]

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)

# XGBoost
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)
acc_xgb = accuracy_score(y_test, y_pred_xgb)

# Resultados
print("Random Forest Accuracy:", round(acc_rf, 4))
print("XGBoost Accuracy:", round(acc_xgb, 4))

print("\nClassification Report - Random Forest")
print(classification_report(y_test, y_pred_rf))

print("\nClassification Report - XGBoost")
print(classification_report(y_test, y_pred_xgb))
