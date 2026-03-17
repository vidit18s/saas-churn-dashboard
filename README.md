# 📊 SaaS Revenue & Churn Analytics Dashboard
🚀 **[Live Demo →](https://saas-churn-dashboard-demo.streamlit.app/)**

An interactive analytics dashboard to analyse customer churn, ARR movements, and revenue performance across a SaaS business — directly relevant to commercial analytics roles in PE-backed and growth-stage SaaS companies.

---

## 📊 Key Metrics Tracked

| Metric | Description |
|--------|-------------|
| Total ARR | Annualised recurring revenue across all segments |
| Churn Rate | Monthly churn by SMB, Mid-Market, Enterprise |
| NRR | Net Revenue Retention across cohorts |
| LTV | Average customer lifetime value |
| NPS vs Churn | Satisfaction score linked to churn risk |

**Realistic SaaS benchmarks used:**
- SMB churn ~3.2% monthly
- Mid-Market churn ~1.8% monthly  
- Enterprise churn ~0.6% monthly

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

| Tool | Purpose |
|------|---------|
| Python | Data generation, transformation, pipeline |
| Pandas & NumPy | Data cleaning and analysis |
| Streamlit | Interactive dashboard |
| Plotly | Charts and visualisations |

---

## ✨ Dashboard Features

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

## 🚀 How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/vidit18s/saas-churn-dashboard.git
cd saas-churn-dashboard
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Generate the data**
```bash
python generate_data.py
```

**5. Run the dashboard**
```bash
streamlit run app.py
```

---

## 📁 Project Structure
```
saas-churn-dashboard/
│
├── generate_data.py       # Synthetic SaaS data generator
├── app.py                 # Streamlit dashboard
├── requirements.txt       # Dependencies
└── README.md
```

---

## 💼 Business Context

This project simulates the kind of commercial data analysis required in SaaS analytics roles — reconciling customer, revenue, and behavioural data to surface actionable insights on churn drivers, revenue health, and segment performance.

---

*Independent project | Vidit Malhotra*  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/viditmalhotra)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/vidit18s)
