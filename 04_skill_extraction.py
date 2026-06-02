import re
import pandas as pd
from sqlalchemy import create_engine

DB_PATH  = "data/job_market.db"
OUT_PATH = "data/skills_extracted.csv"

SKILL_PATTERNS = {
    "python": r"\bpython\b", "sql": r"\bsql\b",
    "excel": r"\bexcel\b", "power_bi": r"\bpower bi\b|\bpowerbi\b",
    "tableau": r"\btableau\b", "aws": r"\baws\b",
    "azure": r"\bazure\b", "machine_learning": r"\bmachine learning\b",
    "agile": r"\bagile\b|\bscrum\b", "jira": r"\bjira\b",
    "communication": r"\bcommunication\b", "leadership": r"\bleadership\b",
    "stakeholder": r"\bstakeholder\b", "snowflake": r"\bsnowflake\b",
    "spark": r"\bpyspark\b|\bapache spark\b",
}

def extract_skills(text):
    if not isinstance(text, str):
        return {s: 0 for s in SKILL_PATTERNS}
    text_lower = text.lower()
    return {skill: int(bool(re.search(pattern, text_lower))) for skill, pattern in SKILL_PATTERNS.items()}

engine = create_engine(f"sqlite:///{DB_PATH}")
df = pd.read_sql("SELECT job_id, title, formatted_experience_level, remote_allowed, applies, description, skills_desc FROM job_postings", engine)
df["full_text"] = df["description"].fillna("") + " " + df["skills_desc"].fillna("")

print(f"Extracting skills from {len(df):,} rows...")
skills_df = pd.DataFrame(df["full_text"].apply(extract_skills).tolist())
result = pd.concat([df[["job_id","title","formatted_experience_level","remote_allowed","applies"]].reset_index(drop=True), skills_df], axis=1)

threshold = result["applies"].quantile(0.75)
result["high_demand"] = (result["applies"] >= threshold).astype(int)
result.to_csv(OUT_PATH, index=False)
print(f"Saved: {OUT_PATH}")
