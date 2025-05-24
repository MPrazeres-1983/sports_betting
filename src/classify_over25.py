
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Carregar dados
df = pd.read_csv("data/ppl_matches_clean.csv")

# Separar colunas de golos
df[["home_goals", "away_goals"]] = df["full_time_score"].str.split("-", expand=True).astype(int)

# Criar target: 1 se total de golos > 2.5, caso contrário 0
df["total_goals"] = df["home_goals"] + df["away_goals"]
df["over_2_5"] = (df["total_goals"] > 2.5).astype(int)

# Codificar nomes de equipas como números
le = LabelEncoder()
df["home_team_encoded"] = le.fit_transform(df["home_team"])
df["away_team_encoded"] = le.fit_transform(df["away_team"])

# Features e target
X = df[["home_team_encoded", "away_team_encoded"]]
y = df["over_2_5"]

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo 1: Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)

# Modelo 2: Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)

# Resultados
print("Logistic Regression Accuracy:", round(acc_lr, 4))
print("Random Forest Accuracy:", round(acc_rf, 4))

print("\nClassification Report - Logistic Regression")
print(classification_report(y_test, y_pred_lr))

print("\nClassification Report - Random Forest")
print(classification_report(y_test, y_pred_rf))
