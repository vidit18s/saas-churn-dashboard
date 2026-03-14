# SaaS Revenue & Churn Analytics Dashboard

An interactive analytics dashboard built to analyse customer churn, ARR movements, and revenue performance across a SaaS business — directly relevant to commercial analytics roles in PE-backed and growth-stage SaaS companies.

Built by **Vidit Malhotra** | MSc Data Science & AI (Distinction), University of Liverpool

🔗 [LinkedIn](https://www.linkedin.com/in/viditmalhotra) | [GitHub](https://github.com/vidit1806)

---

## What this project demonstrates

- End-to-end data pipeline from raw generation to interactive dashboard
- SaaS commercial metrics: ARR, MRR, churn rate, NPS, LTV, Net Revenue Retention
- Segment-level analysis (SMB, Mid-Market, Enterprise)
- Cohort-style retention and churn trend analysis
- Data validation and quality checks on 500+ customer records
- Clean, interactive UI with real-time filters

---

## Tech stack

| Tool | Purpose |
|------|---------|
| Python | Data generation, transformation, pipeline |
| Pandas & NumPy | Data cleaning and analysis |
| Streamlit | Interactive dashboard |
| Plotly | Charts and visualisations |
| Git & GitHub | Version control |

---

## Dashboard features

- **Key metrics** — Total ARR, active customers, churn rate, NRR, avg LTV
- **ARR by segment** — Revenue breakdown across SMB, Mid-Market, Enterprise
- **Churn rate by segment** — Comparative churn across customer tiers
- **Monthly churn trend** — Time-series view of customer losses
- **ARR distribution** — Histogram showing revenue spread by segment
- **NPS vs churn risk** — Scatter plot linking satisfaction scores to churn
- **Revenue by industry** — Horizontal bar chart of ARR by vertical
- **Customer records table** — Filterable, sortable raw data view
- **Sidebar filters** — Filter by segment, industry, and customer status in real time

---

## How to run locally
```bash
git clone https://github.com/vidit1806/saas-churn-dashboard.git
cd saas-churn-dashboard
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python generate_data.py
streamlit run app.py
```

---

## Project structure
```
saas-churn-dashboard/
│
├── data/                  # Generated customer dataset (CSV)
├── notebooks/             # Exploratory analysis (coming soon)
├── generate_data.py       # Synthetic SaaS data generator
├── app.py                 # Streamlit dashboard
├── requirements.txt       # Dependencies
└── README.md              # This file
```

---

## Business context

This project simulates the kind of commercial data analysis required in SaaS analytics roles — reconciling customer, revenue, and behavioural data to surface actionable insights on churn drivers, revenue health, and segment performance.

The dataset is synthetically generated using realistic SaaS benchmarks:
- SMB churn ~3.2% monthly
- Mid-Market churn ~1.8% monthly  
- Enterprise churn ~0.6% monthly
- ARR ranges consistent with typical SaaS pricing tiers