
# ⚽ Sports Betting - Previsão de Over 2.5 Golos com Machine Learning

Este projeto utiliza dados reais da Primeira Liga (Portugal) e aplica modelos de Machine Learning para prever se um jogo terá mais de 2.5 golos. Inclui análise de dados, treino de modelos (Random Forest, XGBoost) e um simulador interativo.

---

## 🚀 Funcionalidades

- Previsão de Over/Under 2.5 golos com base em dados históricos
- Modelos treinados com `XGBoost` e `Random Forest`
- Simulador interativo em terminal
- Script com seleção automática de equipas e previsão estatística
- Preparado para evoluir para aplicação web (Flask)

---

## 📁 Estrutura

```
sports_betting/
├── data/
│   ├── ppl_all_matches.csv           # Jogos reais da Primeira Liga
│   └── ppl_all_enriched.csv         # Dados com médias móveis por equipa
│
├── src/
│   ├── fetch_fd_data.py             # Recolha de dados via API
│   ├── create_enriched_csv.py       # Cálculo de médias móveis
│   ├── train_all_enriched_model.py  # Treino de modelos
│   ├── predict_by_teams.py          # Simulador com escolha de equipas
│   └── simulator_predict_match.py   # Simulador manual com input de médias
│
├── README.md
└── requirements.txt
```

---

## 🧠 Modelos utilizados

- `RandomForestClassifier`
- `XGBClassifier` (XGBoost)

As features utilizadas incluem:
- Média de golos marcados e sofridos por equipa
- Diferença ofensiva e defensiva
- Soma dos ataques (indicador de jogo aberto)

---

## 🧪 Como testar localmente

1. Instala as dependências:

```bash
pip install -r requirements.txt
```

2. Corre o simulador com equipas:

```bash
python src/predict_by_teams.py
```

3. Ou usa o simulador com input manual:

```bash
python src/simulator_predict_match.py
```

---

## 📦 Dependências principais

- `pandas`
- `xgboost`
- `scikit-learn`
- `flask` (para versão web)

---

## 👨‍💻 Autor

Projeto desenvolvido por Mário Prazeres como exercício de aplicação prática de Machine Learning e análise preditiva de desporto.

---
