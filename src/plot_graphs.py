import pandas as pd
import matplotlib.pyplot as plt

# Corrigir leitura da coluna sem cabeçalho
df_vitorias = pd.read_csv("data/wins_by_team.csv", header=None, names=["team", "wins"])

# Remover entradas inválidas
df_vitorias = df_vitorias[df_vitorias["team"].str.lower() != "winner"]

# Ordenar por número de vitórias (opcional)
df_vitorias = df_vitorias.sort_values(by="wins", ascending=False)

import pandas as pd
import matplotlib.pyplot as plt

# Carregar vitórias sem cabeçalho e dar nomes
df_vitorias = pd.read_csv("data/wins_by_team.csv", header=None, names=["team", "wins"])

# Remover linhas inválidas (empates ou headers acidentais)
df_vitorias = df_vitorias[~df_vitorias["team"].isin(["Draw", "winner", "Winner"])]

# Converter 'wins' para inteiro (corrige problemas de tipo)
df_vitorias["wins"] = pd.to_numeric(df_vitorias["wins"], errors="coerce")

# Remover valores nulos
df_vitorias = df_vitorias.dropna()

# Ordenar do maior para o menor
df_vitorias = df_vitorias.sort_values(by="wins", ascending=False)

# Gerar gráfico
plt.figure(figsize=(14, 6))
plt.bar(df_vitorias["team"], df_vitorias["wins"], color="royalblue")
plt.title("Vitórias por Equipa - Primeira Liga (dados reais)")
plt.xlabel("Equipa")
plt.ylabel("Número de Vitórias")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("data/vitorias_por_equipa.png")
plt.close()

print("✔ Gráfico final limpo e corrigido gerado em data/vitorias_por_equipa.png")


# Gráfico circular permanece igual
df_stats = pd.read_csv("data/stats_summary.csv")
jogos_mais_2_5 = df_stats["jogos_mais_2_5_golos"].values[0]
jogos_totais = df_stats["jogos_totais"].values[0]
jogos_outros = jogos_totais - jogos_mais_2_5

plt.figure(figsize=(6, 6))
plt.pie(
    [jogos_mais_2_5, jogos_outros],
    labels=["> 2.5 Golos", "<= 2.5 Golos"],
    autopct="%1.1f%%",
    colors=["green", "red"],
)
plt.title("Distribuição de Jogos com Mais de 2.5 Golos")
plt.savefig("data/distribuicao_golos.png")
plt.close()

print("✔ Gráficos corrigidos e guardados:")
print("- data/vitorias_por_equipa.png")
print("- data/distribuicao_golos.png")
