import pandas as pd
from sqlalchemy import create_engine
import os

DATA_PATH = "data/job_postings.csv"
DB_PATH   = "data/job_market.db"

os.makedirs("data", exist_ok=True)

print("Loading CSV...")
df = pd.read_csv(DATA_PATH, low_memory=False)
print(f"Rows: {len(df):,}  |  Columns: {df.shape[1]}")

df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

keep = [
    "job_id", "title", "company_name", "location", "remote_allowed",
    "formatted_experience_level", "formatted_work_type",
    "applies", "views", "listed_time", "expiry",
    "description", "skills_desc",
    "min_salary", "max_salary", "pay_period", "currency"
]
keep = [c for c in keep if c in df.columns]
df = df[keep].copy()

if "listed_time" in df.columns:
    df["listed_time"] = pd.to_datetime(df["listed_time"], unit="ms", errors="coerce")
if "expiry" in df.columns:
    df["expiry"] = pd.to_datetime(df["expiry"], unit="ms", errors="coerce")

engine = create_engine(f"sqlite:///{DB_PATH}")
df.to_sql("job_postings", engine, if_exists="replace", index=False)
print(f"Saved to SQLite: {DB_PATH}")
print(f"Rows: {len(df):,}")
