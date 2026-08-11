
import pandas as pd
import re

# ======================================================
# LOAD DATASETS
# ======================================================

internshala = pd.read_csv("data/raw/internshala_jobs.csv")

# Load Naukri only if it exists
try:
    naukri = pd.read_csv("data/raw/naukri_jobs.csv")
    df = pd.concat([internshala, naukri], ignore_index=True)
    print("Internshala + Naukri Loaded")
except:
    df = internshala.copy()
    print("Only Internshala Loaded")

print(f"\nOriginal Rows : {len(df)}")

# ======================================================
# REMOVE DUPLICATES
# ======================================================

df = df.drop_duplicates(
    subset=["title", "company"],
    keep="first"
)

print(f"Rows after removing duplicates : {len(df)}")

# ======================================================
# HANDLE MISSING VALUES
# ======================================================

df["ppo"] = df["ppo"].fillna("No PPO Mentioned")

df["skills_required"] = df["skills_required"].fillna("")

df["description"] = df["description"].fillna("")

# ======================================================
# STANDARDIZE TEXT
# ======================================================

for col in ["title",
            "company",
            "skills_required",
            "description"]:

    df[col] = (
        df[col]
        .astype(str)
        .str.lower()
        .str.strip()
    )

# ======================================================
# MERGE SKILLS + DESCRIPTION
# ======================================================

df["combined_text"] = (
    df["skills_required"] +
    " " +
    df["description"]
)

# ======================================================
# NORMALIZATION DICTIONARY
# ======================================================

replacements = {

    r"ms[- ]?excel": "excel",
    r"microsoft excel": "excel",
    r"advanced excel": "excel",

    r"power[- ]?bi": "power bi",
    r"powerbi": "power bi",

    r"tableau software": "tableau",

    r"mysql": "sql",
    r"postgresql": "sql",
    r"postgres": "sql",
    r"sql server": "sql",

    r"python programming": "python",
    r"python3": "python",

    r"machine learning": "machine learning",

    r"data analysis": "data analytics",

    r"effective communication": "communication",
    r"english proficiency \(spoken\)": "communication",
    r"english proficiency \(written\)": "communication",

}

for pattern, replacement in replacements.items():

    df["combined_text"] = df["combined_text"].str.replace(
        pattern,
        replacement,
        regex=True
    )

# ======================================================
# TARGET SKILLS
# ======================================================

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

# ======================================================
# CREATE BINARY SKILL MATRIX
# ======================================================

binary_df = df.copy()

for skill in TARGET_SKILLS:

    binary_df[skill] = binary_df["combined_text"].str.contains(
        re.escape(skill),
        case=False,
        na=False
    ).astype(int)

# ======================================================
# SAVE CLEAN DATASET
# ======================================================

clean_columns = [

    "role",

    "title",

    "company",

    "location",

    "stipend",

    "duration",

    "skills_required",

    "description",

    "ppo",

    "source"

]

df[clean_columns].to_csv(

    "data/processed/clean_jobs.csv",

    index=False,

    encoding="utf-8-sig"

)

# ======================================================
# SAVE BINARY MATRIX
# ======================================================

matrix_columns = [

    "role",

    "title",

    "company"

] + TARGET_SKILLS

binary_df[matrix_columns].to_csv(

    "data/processed/binary_skill_matrix.csv",

    index=False,

    encoding="utf-8-sig"

)

print("\n" + "="*60)

print("PREPROCESSING COMPLETE")

print("="*60)

print(f"Clean Dataset Rows : {len(df)}")

print(f"Binary Matrix Rows : {len(binary_df)}")

print("\nFiles Generated")

print("✓ clean_jobs.csv")

print("✓ binary_skill_matrix.csv")