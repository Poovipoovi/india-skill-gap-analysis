import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://internshala.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

roles = [
    "data-analyst",
    "data-science",
    "business-analyst"
]

links = set()

for role in roles:

    print(f"\nScraping {role}")

    for page in range(1, 6):

        url = f"{BASE_URL}/internships/{role}-internship/page-{page}"

        response = requests.get(url, headers=headers, timeout=20)

        print(f"Page {page} --> {response.status_code}")

        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        job_links = soup.find_all(
            "a",
            class_="job-title-href"
        )

        print(f"Found {len(job_links)} internship links")

        for job in job_links:

            href = job.get("href")

            if href:

                if href.startswith("/"):

                    href = BASE_URL + href

                links.add(href)

        time.sleep(2)

print("\nFinished")
print(f"Unique links collected : {len(links)}")

df = pd.DataFrame({
    "link": list(links)
})

df.to_csv(
    "data/raw/internship_links.csv",
    index=False
)

