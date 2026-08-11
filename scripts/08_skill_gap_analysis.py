import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================

industry = pd.read_csv("data/processed/skill_frequency.csv")
college = pd.read_csv("data/raw/college_scores.csv")

# =====================================================
# MAP SKILL NAMES
# =====================================================

mapping = {
    "SQL": "sql",
    "Excel": "excel",
    "Power BI": "power bi",
    "Tableau": "tableau",
    "Python": "python",
    "Statistics": "statistics",
    "Data Analytics": "data analytics",
    "Machine Learning": "machine learning",
    "Data Visualization": "data visualization",
    "ETL": "etl",
    "Communication": "communication",
    "Problem Solving": "problem solving"
}

# =====================================================
# CALCULATE COLLEGE COVERAGE
# =====================================================

results = []

total_colleges = len(college)

for college_skill, industry_skill in mapping.items():

    # Number of colleges teaching this skill
    covered = (college[college_skill] > 0).sum()

    coverage_percent = round((covered / total_colleges) * 100, 2)

    demand = industry.loc[
        industry["Skill"].str.lower() == industry_skill,
        "Demand (%)"
    ].values

    if len(demand) == 0:
        demand = 0
    else:
        demand = round(float(demand[0]), 2)

    gap = round(demand - coverage_percent, 2)

    # Classification
    if demand >= 15 and coverage_percent < 50:
        status = "Critical Gap"

    elif demand >= 15 and coverage_percent >= 50:
        status = "Well Covered"

    elif demand < 15 and coverage_percent < 50:
        status = "Low Priority"

    else:
        status = "Moderately Covered"

    results.append({
        "Skill": college_skill,
        "Industry Demand (%)": demand,
        "College Coverage (%)": coverage_percent,
        "Gap": gap,
        "Status": status
    })

# =====================================================
# SAVE
# =====================================================

result_df = pd.DataFrame(results)

result_df = result_df.sort_values(
    by="Industry Demand (%)",
    ascending=False
)

result_df.to_csv(
    "data/processed/skill_gap_analysis.csv",
    index=False
)

print("\nSKILL GAP ANALYSIS COMPLETE")
print("="*60)

print(result_df)