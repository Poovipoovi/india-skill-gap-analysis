# India Skill Gap Analysis

**<h2>📊Dashboard preview</h2>**
<img width="1587" height="918" alt="dashboard_preview" src="https://github.com/user-attachments/assets/f68d9c41-da5c-428a-8ed2-cf37e23995f4" />


## 📌 Project Overview

**India Skill Gap Analysis** is a data analytics project that studies the gap between **skills demanded by the industry** and the **skills covered in engineering college curricula**.

The project analyzes job postings for data and analytics-related roles and compares the skills frequently requested by employers with the skills present in the curricula of selected engineering colleges.

The objective is to identify:

* Which technical and professional skills are most demanded by industry
* Which skills are adequately represented in college curricula
* Which skills have limited or missing curriculum coverage
* Which skills should receive greater attention when designing or updating engineering curricula

The final outcome is an interactive **Power BI dashboard** that presents the major findings in a concise and visual form.

---

## 🎯 Problem Statement

The technology industry changes rapidly, with employers continuously introducing new tools, technologies, and skill requirements.

However, academic curricula may not always evolve at the same pace. This can create a **skill gap** between what students learn during their engineering education and what employers expect from graduates.

Traditional curriculum evaluation is often based on manual comparisons and subjective assessments. A data-driven approach can provide a more systematic way of identifying differences between industry requirements and academic skill coverage.

This project attempts to address this problem by analyzing real-world job posting data and comparing the resulting skill demand with engineering curriculum data.

---

## 💡 Proposed Solution

The proposed solution follows a data-driven workflow:

Job Postings
     ↓
Data Collection
     ↓
Data Cleaning & Preprocessing
     ↓
Skill Extraction
     ↓
Industry Skill Demand Analysis
     ↓
Curriculum Skill Extraction
     ↓
Industry vs Curriculum Comparison
     ↓
Skill Gap Classification
     ↓
Power BI Dashboard


The system produces quantitative insights that can help identify areas where curriculum coverage may need improvement.

---

## 🔍 Key Questions

The project attempts to answer the following questions:

1. What skills are most frequently demanded in data and analytics-related job postings?
2. Which skills appear most consistently across job descriptions?
3. How well are these skills represented in selected engineering curricula?
4. Which skills show significant gaps between industry demand and curriculum coverage?
5. Which skills require greater attention from curriculum designers?
6. What overall patterns can be observed between industry requirements and academic education?

---

# 📊 Dataset

The project uses multiple datasets generated and processed during the analysis pipeline.

### Job Posting Data

Job postings were collected from online job/internship sources and processed to extract relevant information.

The repository contains:

data/raw/
├── internshala_jobs.csv
├── naukri_jobs.csv
├── job_descriptions.csv
└── internship_links.csv


A combined and cleaned dataset is produced during preprocessing.

### Curriculum Data

Curriculum information from selected engineering programs is used to identify the skills covered academically.

data/curricula/
└── curriculum_skills.xlsx


### Processed Datasets

The project generates several intermediate and final datasets:

data/processed/
├── clean_jobs.csv
├── binary_skill_matrix.csv
├── college_alignment_scores.csv
├── college_skill_gap.csv
├── curriculum_dataset.csv
├── final_dataset.csv
├── skill_frequency.csv
└── skill_gap_analysis.csv

---

# 🧹 Data Processing

The raw job posting data cannot be directly used for analysis because job postings may contain:

* Missing values
* Duplicate records
* Different representations of the same skill
* Unnecessary text
* Inconsistent formatting
* Irrelevant job-posting information

Therefore, the project performs data preprocessing before analysis.

### Main preprocessing operations

* Combining data from different sources
* Removing duplicate records
* Handling missing values
* Cleaning job descriptions
* Standardizing skill names
* Extracting relevant skills
* Creating structured skill indicators
* Preparing datasets for analysis

---

# 🛠️ Skill Extraction

A predefined set of relevant skills is used to identify skills appearing in job descriptions.

Examples include:

* Python
* SQL
* Excel
* Power BI
* Tableau
* Machine Learning
* Data Analytics
* Statistics
* ETL
* Communication
* Problem Solving
* and other relevant skills

A **binary skill matrix** is generated where the presence of a skill in a job posting is represented using a binary indicator.

Example:

| Job   | Python | SQL | Excel | Power BI |
| ----- | -----: | --: | ----: | -------: |
| Job 1 |      1 |   1 |     1 |        0 |
| Job 2 |      1 |   1 |     0 |        1 |
| Job 3 |      0 |   1 |     1 |        0 |

This allows the project to calculate how frequently each skill appears across the collected job postings.

---

# 📈 Industry Skill Demand Analysis

The frequency of each skill is calculated from the processed job-posting dataset.

The frequency analysis helps determine which skills are most commonly requested by employers.

The resulting dataset is stored in:
data/processed/skill_frequency.csv


This forms the industry-demand side of the analysis.

---

# 🎓 Curriculum Skill Analysis

The skills identified in engineering curricula are structured and compared against the industry skill list.

The curriculum analysis determines whether a particular skill is:

* Covered
* Partially represented
* Not covered
* or otherwise categorized according to the project's gap-analysis methodology

The processed curriculum information is stored in:
data/processed/curriculum_dataset.csv


---

# ⚖️ Skill Gap Analysis

The project compares industry demand with curriculum coverage.

The resulting analysis is stored in:

data/processed/skill_gap_analysis.csv

The analysis categorizes skills based on their relationship between industry demand and curriculum coverage.

The dashboard presents these categories through a **Skill Gap Distribution** visualization and a detailed **Skill Coverage Analysis** table.

---

# 📊 Power BI Dashboard

The final analysis is presented through an interactive Power BI dashboard.

Power BI file:

dashboard/india_skill_gap.pbix


### Dashboard components

#### 1. KPI Cards

The dashboard provides high-level project metrics such as:

* Number of job postings analyzed
* Number of skills analyzed
* Number of curricula compared
* Number of critical skill gaps

These provide an immediate overview of the analysis.

---

#### 2. Top Skills by Industry Demand

A bar chart displays the skills most frequently demanded in the analyzed job postings.

This answers:

> **What skills does the industry demand most?**

---

#### 3. Skill Gap Distribution

A donut chart summarizes the distribution of analyzed skills according to their curriculum-gap categories.

This provides a quick overview of the overall skill-gap situation.

---

#### 4. Skill Coverage Analysis

A detailed table provides skill-level information including:

* Skill
* Industry Demand
* Gap
* Status

This allows users to move from the high-level dashboard insights to individual skill-level analysis.

---

#### 5. Key Insights

The dashboard summarizes the most important findings from the analysis so that users can understand the practical implications without interpreting every individual chart.

---

# 🧰 Technologies Used

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Power BI

### Data Storage / Processing

* CSV
* Excel

### Development Tools

* Git
* GitHub
* VS Code / Python development environment

---

# 📁 Project Structure

India's_skill_gap_analysis/
│
├── dashboard/
│   └── india_skill_gap.pbix
│
├── data/
│   │
│   ├── curricula/
│   │   └── curriculum_skills.xlsx
│   │
│   ├── job_postings/
│   │   └── job_postings_sample.xlsx
│   │
│   ├── processed/
│   │   ├── binary_skill_matrix.csv
│   │   ├── clean_jobs.csv
│   │   ├── college_alignment_scores.csv
│   │   ├── college_skill_gap.csv
│   │   ├── curriculum_dataset.csv
│   │   ├── final_dataset.csv
│   │   ├── skill_frequency.csv
│   │   └── skill_gap_analysis.csv
│   │
│   └── raw/
│       ├── college_scores.csv
│       ├── internshala_jobs.csv
│       ├── internship_links.csv
│       ├── job_descriptions.csv
│       └── naukri_jobs.csv
│
├── scripts/
│   ├── 01_scrape_links.py
│   ├── 02_scrape_internshala.py
│   ├── 03_scrape_naukri.py
│   ├── 04_combine_clean.py
│   ├── 05_skill_frequency.py
│   ├── 06_skill_gap_analysis.py
│   ├── 07_visualization.py
│   ├── 08_skill_gap_analysis.py
│   └── verify_dataset.py
│
├── .gitignore
└── README.md


---

# 🔄 Project Pipeline

The complete implementation is divided into the following stages.

### Stage 1 — Data Collection

Collect job posting information from relevant online sources and gather curriculum information from selected engineering programs.

### Stage 2 — Data Cleaning

Combine and clean the collected job-posting data.

### Stage 3 — Skill Extraction

Identify predefined skills from job descriptions and create a structured binary skill matrix.

### Stage 4 — Industry Demand Analysis

Calculate skill frequencies to determine the most demanded skills.

### Stage 5 — Curriculum Analysis

Extract and structure skills present in the selected engineering curricula.

### Stage 6 — Gap Analysis

Compare industry demand and curriculum coverage to identify skill gaps.

### Stage 7 — Visualization

Generate supporting visualizations and analytical datasets.

### Stage 8 — Dashboard Development

Build the final Power BI dashboard to communicate the findings.

---

# 📌 Key Findings

The current analysis identifies several important patterns between industry requirements and academic curriculum coverage.

The dashboard highlights:

* Highly demanded industry skills
* Skills with limited curriculum representation
* Critical skill gaps
* Overall distribution of skill-gap categories
* Skill-level differences between industry requirements and academic coverage

The exact findings are presented dynamically through the Power BI dashboard and processed datasets.

---

# 🎯 Project Impact

The project can provide useful information for:

### Universities and Curriculum Designers

Identify skills that may require stronger representation in engineering curricula.

### Students

Understand which skills are frequently requested by employers and prioritize their learning accordingly.

### Educators

Use industry data as an additional reference when evaluating curriculum relevance.

### Researchers

Use the analysis as a foundation for studying the relationship between higher education and changing industry skill requirements.

---

# ⚠️ Limitations

This project has several limitations that should be considered when interpreting the results.

### 1. Job Posting Coverage

The analysis is based on the job postings collected during the project and therefore does not represent every job available in India.

### 2. Source Bias

Different job platforms may have different types of employers, roles, and posting patterns. Therefore, the collected sample may contain source-specific bias.

### 3. Skill Extraction

Skill identification depends on the predefined skill list and the methodology used to extract skills from job descriptions. Skills that are not included in the predefined list may not appear in the final analysis.

### 4. Curriculum Representation

Curriculum documents may describe subjects differently, and the presence of a skill in a curriculum does not necessarily indicate the depth or quality of its coverage.

### 5. Gap Interpretation

The calculated skill gap should be interpreted as an analytical comparison of the collected industry-demand and curriculum data, rather than as an absolute measure of curriculum quality.

---

# 🚀 Future Enhancements

Possible future improvements include:

* Expanding the number of job postings
* Adding additional job platforms
* Including more engineering colleges and universities
* Automatically extracting skills using NLP techniques
* Incorporating emerging technologies and new skill categories
* Performing analysis across different job roles
* Performing location-wise skill-demand analysis
* Tracking skill demand over time
* Developing a web-based version of the dashboard
* Adding automated curriculum recommendations

---

# 👩‍💻 Authors

**Poovizhi A**

Computer Science and Engineering

---

# 📄 License

This project is developed for **academic and educational purposes**.
