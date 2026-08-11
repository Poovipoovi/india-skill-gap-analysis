import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/internshala_jobs.csv")

print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(f"\nRows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

print("\n" + "=" * 60)
print("EMPTY STRINGS")
print("=" * 60)

for col in df.columns:
    empty = (df[col].astype(str).str.strip() == "").sum()
    print(f"{col:<20} : {empty}")

print("\n" + "=" * 60)
print("UNIQUE COMPANIES")
print("=" * 60)

print(df["company"].nunique())

print("\n" + "=" * 60)
print("TOP 10 SKILLS")
print("=" * 60)

all_skills = []

for skills in df["skills_required"].dropna():
    for skill in skills.split(","):
        skill = skill.strip().lower()
        if skill:
            all_skills.append(skill)

skill_freq = (
    pd.Series(all_skills)
    .value_counts()
    .head(10)
)

print(skill_freq)

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

duplicates = df.duplicated().sum()
print(f"Duplicate rows : {duplicates}")

print("\nVerification Complete.")