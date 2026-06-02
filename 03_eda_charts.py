import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from sqlalchemy import create_engine
import os

os.makedirs("outputs/charts", exist_ok=True)
engine = create_engine("sqlite:///data/job_market.db")

PALETTE = ["#534AB7", "#1D9E75", "#D85A30", "#BA7517", "#185FA5", "#993556"]

def sql(query):
    return pd.read_sql(query, engine)

# Chart 1 - Top job titles
df1 = sql("SELECT title, COUNT(*) AS count FROM job_postings WHERE title IS NOT NULL GROUP BY title ORDER BY count DESC LIMIT 15")
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df1["title"][::-1], df1["count"][::-1], color=PALETTE[0], height=0.6)
ax.bar_label(bars, fmt="{:,.0f}", padding=4, fontsize=9)
ax.set_title("Top 15 Job Titles by Posting Volume", fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/charts/01_top_job_titles.png", dpi=150)
plt.close()

# Chart 2 - Experience level
df2 = sql("SELECT formatted_experience_level AS level, COUNT(*) AS count FROM job_postings WHERE formatted_experience_level IS NOT NULL GROUP BY level ORDER BY count DESC")
fig, ax = plt.subplots(figsize=(8, 5))
ax.pie(df2["count"], labels=df2["level"], autopct="%1.1f%%", colors=PALETTE, startangle=140, wedgeprops={"linewidth": 0.5, "edgecolor": "white"})
ax.set_title("Job Postings by Experience Level", fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/charts/02_experience_level.png", dpi=150)
plt.close()

# Chart 3 - Remote vs onsite
df3 = sql("SELECT CASE WHEN remote_allowed=1 THEN 'Remote' WHEN remote_allowed=0 THEN 'On-site' ELSE 'Not specified' END AS mode, COUNT(*) AS count FROM job_postings GROUP BY remote_allowed")
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(df3["mode"], df3["count"], color=[PALETTE[1], PALETTE[0], PALETTE[2]][:len(df3)], width=0.5)
ax.bar_label(bars, fmt="{:,.0f}", padding=4)
ax.set_title("Remote vs On-site Job Postings", fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/charts/03_remote_vs_onsite.png", dpi=150)
plt.close()

# Chart 4 - Top locations
df4 = sql("SELECT location, COUNT(*) AS count FROM job_postings WHERE location IS NOT NULL GROUP BY location ORDER BY count DESC LIMIT 10")
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(df4["location"][::-1], df4["count"][::-1], color=PALETTE[2], height=0.6)
ax.bar_label(bars, fmt="{:,.0f}", padding=4, fontsize=9)
ax.set_title("Top 10 Locations by Job Posting Volume", fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/charts/06_top_locations.png", dpi=150)
plt.close()

print("All charts saved to outputs/charts/")
