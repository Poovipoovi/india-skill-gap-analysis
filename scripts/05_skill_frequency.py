import pandas as pd

# ==========================
# LOAD BINARY MATRIX
# ==========================

df = pd.read_csv("data/processed/binary_skill_matrix.csv")

TARGET_SKILLS = [

    "sql",
    "excel",
    "power bi",
    "tableau",
    "python",
    "statistics",
    "data analytics",
    "machine learning",
    "data visualization",
    "etl",
    "communication",
    "problem solving"

]

# ==========================
# CALCULATE FREQUENCY
# ==========================

results = []

total_jobs = len(df)

for skill in TARGET_SKILLS:

    frequency = int(df[skill].sum())

    percentage = round(
        (frequency / total_jobs) * 100,
        2
    )

    results.append({

        "Skill": skill,

        "Frequency": frequency,

        "Demand (%)": percentage

    })

frequency_df = pd.DataFrame(results)

frequency_df = frequency_df.sort_values(

    by="Frequency",

    ascending=False

)

# ==========================
# SAVE
# ==========================

frequency_df.to_csv(

    "data/processed/skill_frequency.csv",

    index=False,

    encoding="utf-8-sig"

)

print("=" * 60)

print("SKILL FREQUENCY")

print("=" * 60)

print(frequency_df)

print("\nSaved Successfully!")
