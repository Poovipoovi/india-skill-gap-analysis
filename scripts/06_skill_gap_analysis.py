import pandas as pd

# ==========================================================
# LOAD DATA
# ==========================================================

industry = pd.read_csv("data/processed/skill_frequency.csv")
college = pd.read_csv("data/raw/college_scores.csv")

# ==========================================================
# INDUSTRY DEMAND (%) -> INDUSTRY SCORE (0,1,2)
# ==========================================================

def industry_score(demand):

    if demand >= 30:
        return 2

    elif demand >= 10:
        return 1

    else:
        return 0


industry["Industry Score"] = industry["Demand (%)"].apply(industry_score)

# ==========================================================
# COLLEGE SCORE MAP
# ==========================================================

industry_name_map = {

    "sql": "SQL",
    "excel": "Excel",
    "power bi": "Power BI",
    "tableau": "Tableau",
    "python": "Python",
    "statistics": "Statistics",
    "data analytics": "Data Analytics",
    "machine learning": "ML",
    "data visualization": "Data Viz",
    "etl": "ETL",
    "communication": "Communication",
    "problem solving": "Problem Solving"

}

# ==========================================================
# GAP ANALYSIS
# ==========================================================

gap_results = []

for _, college_row in college.iterrows():

    college_name = college_row["College"]

    for _, industry_row in industry.iterrows():

        skill = industry_name_map[industry_row["Skill"]]

        industry_percentage = industry_row["Demand (%)"]

        industry_score_value = industry_row["Industry Score"]

        college_score = college_row[skill]

        gap_score = industry_score_value - college_score

        # Interpretation
        if gap_score > 0:
            interpretation = "Curriculum Behind Industry"

        elif gap_score < 0:
            interpretation = "Curriculum Ahead of Industry"

        else:
            interpretation = "Well Aligned"

        gap_results.append({

            "College": college_name,

            "Skill": skill,

            "Industry Demand (%)": industry_percentage,

            "Industry Score": industry_score_value,

            "College Score": college_score,

            "Gap Score": gap_score,

            "Interpretation": interpretation

        })

# ==========================================================
# CREATE DATAFRAME
# ==========================================================

gap_df = pd.DataFrame(gap_results)

# ==========================================================
# SAVE
# ==========================================================

gap_df.to_csv(
    "data/processed/college_skill_gap.csv",
    index=False,
    encoding="utf-8-sig"
)

print("=" * 70)
print("SKILL GAP ANALYSIS COMPLETE")
print("=" * 70)

print(gap_df.head(20))

print("\nRows :", len(gap_df))

print("\nSaved Successfully!")
print("data/processed/college_skill_gap.csv")