
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Carregar o novo dataset
df = pd.read_csv("data/ppl_all_enriched.csv")

# Features e target
X = df[["media_home_gm", "media_home_gs", "media_away_gm", "media_away_gs"]]
y = df["over_2_5"]

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Regressão Logística
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)

# Random Forest
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
