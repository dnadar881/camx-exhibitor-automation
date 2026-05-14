from scraper import scrape_exhibitors
from generate import generate_first_line
import pandas as pd

data = scrape_exhibitors()

for company in data:
    company["first_line"] = generate_first_line(company)

# Clean descriptions (shorten)
for c in data:
    desc = c["description"].replace("\n", " ")

    # Try extracting after "About"
    if "About" in desc:
        desc = desc.split("About")[-1]

    # fallback: remove navigation noise
    desc = desc.replace("Home", "").replace("Add to Planner", "")

    c["description"] = desc.strip()[:150]

df = pd.DataFrame(data)
df.to_csv("final_output.csv", index=False, encoding="utf-8-sig")

print("✅ CSV ready")
