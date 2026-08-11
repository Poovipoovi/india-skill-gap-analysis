import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ===========================
# Configuration
# ===========================

BASE_URL = "https://internshala.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
}

ROLES = [
    "data-analyst",
    "business-analyst",
    "data-science",
    "data-engineer",
    "machine-learning",
    "artificial-intelligence",
    "business-intelligence",
    "python",
    "analytics",
    "sql",
    "database",
    "power-bi",
    "tableau",
    "data-visualization"
]

PAGES = 10

jobs = []

# ===========================
# Scraping
# ===========================

for role in ROLES:

    print("=" * 70)
    print(f"Scraping Role : {role}")
    print("=" * 70)

    for page in range(1, PAGES + 1):

        url = f"{BASE_URL}/internships/{role}-internship/page-{page}"

        try:

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=20
            )

            print(f"Page {page} | Status Code : {response.status_code}")

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            cards = soup.find_all("div", class_="internship_meta")

            if len(cards) == 0:
                print(f"No internships found on Page {page}")
                break

            print(f"Found {len(cards)} internships")

            for card in cards:

                try:

                    # ------------------------
                    # Title
                    # ------------------------

                    title = card.select_one("a.job-title-href")
                    title = title.get_text(strip=True) if title else ""

                    # ------------------------
                    # Company
                    # ------------------------

                    company = card.select_one("p.company-name")
                    company = company.get_text(strip=True) if company else ""

                    # ------------------------
                    # Location
                    # ------------------------

                    location = card.select_one("div.locations a")
                    location = location.get_text(strip=True) if location else "N/A"

                    # ------------------------
                    # Stipend
                    # ------------------------

                    stipend = card.select_one("span.stipend")
                    stipend = stipend.get_text(strip=True) if stipend else "N/A"

                    # ------------------------
                    # Duration
                    # ------------------------

                    duration = "N/A"

                    row_items = card.select("div.row-1-item span")

                    if len(row_items) >= 3:
                        duration = row_items[2].get_text(strip=True)

                    # ------------------------
                    # Skills
                    # ------------------------

                    skills = card.select("div.job_skill")

                    skill_list = [
                        skill.get_text(strip=True)
                        for skill in skills
                    ]

                    skills_required = ", ".join(skill_list)

                    # ------------------------
                    # Description
                    # ------------------------

                    description = card.select_one("div.about_job div.text")

                    description = (
                        description.get_text(" ", strip=True)
                        if description else ""
                    )

                    # ------------------------
                    # PPO
                    # ------------------------

                    ppo = "No PPO Mentioned"

                    ppo_div = card.find("div", class_="ppo_status")

                    if ppo_div:
                        ppo = ppo_div.get_text(" ", strip=True)

                    # ------------------------
                    # Save Record
                    # ------------------------

                    jobs.append({

                        "role": role,

                        "title": title,

                        "company": company,

                        "location": location,

                        "stipend": stipend,

                        "duration": duration,

                        "skills_required": skills_required,

                        "description": description,

                        "ppo": ppo,

                        "source": "Internshala"

                    })

                except Exception:
                    continue

            time.sleep(2)

        except Exception as e:
            print(e)

# ===========================
# Create DataFrame
# ===========================

df = pd.DataFrame(jobs)

# Remove duplicates
df = df.drop_duplicates(
    subset=["title", "company"],
    keep="first"
)

# Replace missing values
df["ppo"] = df["ppo"].fillna("No PPO Mentioned")
df["skills_required"] = df["skills_required"].fillna("")

# Clean whitespace
for col in df.columns:
    df[col] = df[col].astype(str).str.strip()

# ===========================
# Dataset Summary
# ===========================

print("\n")
print("=" * 70)
print("SCRAPING COMPLETE")
print("=" * 70)

print(f"Total Jobs        : {len(df)}")
print(f"Unique Companies  : {df['company'].nunique()}")

print("\nTop 10 Roles")
print(df["role"].value_counts())

print("\nSample Data")
print(df.head())

# ===========================
# Save CSV
# ===========================

output_path = "data/raw/internshala_jobs.csv"

df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print("\nDataset saved successfully!")
print(output_path)