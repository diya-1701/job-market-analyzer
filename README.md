# Job Market Analyzer — AI-Powered Portfolio Project

**Author:** Diya Gupta | [LinkedIn](https://www.linkedin.com/in/diyagupta17/)  
**Tools:** Python · SQL · scikit-learn · SHAP · Claude API · Power BI  
**Dataset:** LinkedIn Job Postings 2023–2024 (Kaggle, 123,849 rows)

---

## Project Overview

End-to-end data analysis project analyzing 123,849 LinkedIn job postings to identify
in-demand skills, hiring trends, and what drives high application volume — using machine
learning, NLP-based skill extraction, and AI-generated reporting.

---

## Key Findings

- **Remote work** is the single strongest predictor of application volume — carrying
  50% more predictive weight than any individual technical skill (SHAP analysis)
- **Experience level** drives demand more than specific tools or languages
- **Core analyst skills** (Excel, SQL, Communication, Agile) outrank advanced ML
  tools in real-world demand impact
- **87% of postings** don't specify remote status — a gap given it's the #1 demand driver
- ML model achieved **84% accuracy** and **0.697 AUC-ROC** on held-out test data

---

## Project Structure
job_market_analyzer/
├── data/                        # Raw and processed data
├── outputs/
│   ├── charts/                  # 6 EDA visualizations
│   ├── model/                   # ML model outputs + SHAP charts
│   ├── summary/                 # AI-generated executive summary
│   └── powerbi/                 # Power BI ready CSVs
├── sql/
│   └── 02_profiling_queries.sql # SQL profiling queries
├── docs/
│   └── BRD_template.md          # Business Requirements Document
├── 01_load_data.py              # Load CSV into SQLite
├── 03_eda_charts.py             # EDA visualizations
├── 04_skill_extraction.py       # NLP skill extraction
├── 05_ml_model.py               # Random Forest classifier
├── 06_shap_analysis.py          # SHAP explainability
├── 07_ai_summary.py             # LLM-powered executive summary
├── UAT_test_plan.txt            # UAT documentation
└── README.md

---

## Methodology

### Week 1 — Data Foundation
- Loaded 123,849 job postings into SQLite using Python + SQLAlchemy
- Profiled data quality via 10 SQL queries — identified 87% null rate in remote field
- Generated 6 EDA charts across job titles, locations, salary, experience, and trends
- Extracted 35 skills from unstructured job description text using regex/NLP

### Week 2 — AI & ML Layer
- Trained Random Forest classifier to predict high-demand roles (top 25% by applications)
- Applied class_weight=balanced to handle 95/5 class imbalance
- Used SHAP values to explain model outputs in business language
- Integrated Claude API to auto-generate plain-English executive summary from findings

### Week 3 — Dashboard & Documentation
- Built 3-page Power BI dashboard with market overview, skills analysis, and AI insights
- Wrote and executed 15-case UAT plan — identified and resolved 3 defects
- Documented findings in BRD format with AS-IS / TO-BE analysis

---

## Results

| Metric                  | Value       |
|-------------------------|-------------|
| Total postings analyzed | 123,849     |
| Skills tracked          | 35          |
| Model accuracy          | 84%         |
| AUC-ROC score           | 0.697       |
| UAT pass rate           | 100% (15/15)|
| Defects resolved        | 3/3         |

---

## Setup

```bash
pip install pandas sqlalchemy matplotlib seaborn scikit-learn shap tqdm spacy anthropic
python -m spacy download en_core_web_sm
```

Dataset: [LinkedIn Job Postings on Kaggle](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

