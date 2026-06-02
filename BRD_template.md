# Business Requirements Document
## Project: AI-Assisted Job Market Analyzer
**Author:** Diya Gupta | **Date:** June 2026 | **Version:** 1.0

## 1. Executive Summary
Analysis of 123,849 LinkedIn job postings to identify in-demand skills and hiring trends
using ML, NLP, and AI-assisted reporting. Output: Power BI dashboard + predictive model.

## 2. Business Problem
**AS-IS:** Skills buried in unstructured text, no unified view of demand trends,
salary data incomplete (high null rate), remote status unspecified for 87% of postings.

**TO-BE:** Cleaned structured dataset, ML model predicting high-demand roles,
interactive dashboard with skill/industry/level filters, AI-generated executive summary.

## 3. Data Profiling Summary
| Metric                  | Value      |
|-------------------------|------------|
| Total job postings      | 123,849    |
| Missing salary data     | High       |
| Missing skills desc     | Partial    |
| Remote postings         | 12.3%      |
| Most common level       | Mid-Senior |

## 4. Key Findings
1. Remote work is the #1 driver of application volume (SHAP = 0.130)
2. Experience level outweighs any individual technical skill
3. Core analyst skills dominate: Excel, SQL, Communication, Agile
4. 87% of postings don't specify remote status despite it being the top demand driver
5. Python ranks 9th — present but not a primary differentiator at scale

## 5. Success Metrics
| Metric            | Target  | Achieved |
|-------------------|---------|----------|
| Model accuracy    | >75%    | 84%      |
| AUC-ROC           | >0.65   | 0.697    |
| Skills tracked    | >30     | 35       |
| UAT pass rate     | 100%    | 100%     |
| Defects resolved  | 100%    | 3/3      |
