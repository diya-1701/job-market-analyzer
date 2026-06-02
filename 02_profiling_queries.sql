-- SQL Profiling Queries
-- Database: data/job_market.db | Table: job_postings

-- 1. Total rows
SELECT COUNT(*) AS total_rows FROM job_postings;

-- 2. Null rates
SELECT
    COUNT(*) AS total,
    SUM(CASE WHEN title IS NULL THEN 1 ELSE 0 END) AS null_title,
    SUM(CASE WHEN min_salary IS NULL THEN 1 ELSE 0 END) AS null_salary,
    SUM(CASE WHEN skills_desc IS NULL THEN 1 ELSE 0 END) AS null_skills
FROM job_postings;

-- 3. Top job titles
SELECT title, COUNT(*) AS postings FROM job_postings
WHERE title IS NOT NULL GROUP BY title ORDER BY postings DESC LIMIT 20;

-- 4. Experience level breakdown
SELECT formatted_experience_level AS level, COUNT(*) AS postings,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM job_postings), 1) AS pct
FROM job_postings WHERE formatted_experience_level IS NOT NULL
GROUP BY level ORDER BY postings DESC;

-- 5. Remote vs onsite
SELECT CASE WHEN remote_allowed=1 THEN 'Remote'
            WHEN remote_allowed=0 THEN 'On-site'
            ELSE 'Not specified' END AS mode,
    COUNT(*) AS postings
FROM job_postings GROUP BY remote_allowed;

-- 6. Top locations
SELECT location, COUNT(*) AS postings FROM job_postings
WHERE location IS NOT NULL GROUP BY location ORDER BY postings DESC LIMIT 15;
