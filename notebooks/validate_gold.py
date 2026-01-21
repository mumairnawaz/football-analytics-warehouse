import pandas as pd

# =========================
# LOAD GOLD TABLES
# =========================
fact = pd.read_parquet("data/gold/fact_matches.parquet")
league = pd.read_parquet("data/gold/league_kpis.parquet")
teams = pd.read_parquet("data/gold/team_performance.parquet")

# =========================
# BASIC VALIDATION
# =========================
print("Fact matches shape:", fact.shape)
print("League KPIs shape:", league.shape)
print("Team performance shape:", teams.shape)

# =========================
# PREVIEW DATA
# =========================
print("\nLeague KPIs preview:")
print(league.head())

# =========================
# TOP TEAMS ANALYSIS
# =========================
print("\nTop teams by goal difference (per competition & season):")

top_teams = (
    teams.sort_values("goal_difference", ascending=False)
         .groupby(["competition", "season"])
         .head(5)
)

print(top_teams)