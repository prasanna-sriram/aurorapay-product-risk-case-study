# AuroraPay Product Risk Analytics for Real‑Time Payments (ERM, Operational Risk, Fraud, Access Management)

---

### Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Methodology](#methodology)
- [Skills Demonstrated](#skills-demonstrated)
- [Results and Business Recommendations](#results-and-business-recommendations)
- [Next Steps and Extensions](#next-steps-and-extensions)
- [Project Files](#project-files)
- [How to Run](#how-to-run)
- [License](#license)
- [Author Info](#author-info)

---

### Project Overview

AuroraPay is a fictional national, real‑time account‑to‑account payments network inspired by Interac, supporting debit‑like purchases and e‑Transfer‑style money movement between Canadian bank accounts. This project demonstrates how a **Product Risk Lead** can embed **enterprise risk management (ERM)** into a payments product by combining **Python, SQL‑style analytics, and Power BI** to produce a second‑line view of product risk.

Using synthetic transaction, incident, control, and issue data, the project:
- Defines a **product‑aligned risk taxonomy and risk register** for AuroraPay.
- Builds KRIs on **transaction volumes, fraud rates, incidents, and open issues**.
- Visualizes these in **Power BI dashboards**.
- Summarizes the findings in an **executive risk paper** written from a second‑line perspective.

For the full narrative written as an MRC/BRC‑style paper, see:
- [Product Risk Executive Summary](/reports/product_risk_executive_summary.md)

[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

### Business Problem

Real‑time payments rails sit at the center of everyday commerce and are expected to be **always on, secure, and trusted**. A Product Risk Lead embedded with the AuroraPay product squad needs to answer questions like:
- Are outages, fraud events, and control weaknesses staying within our **risk appetite**?
- Where is **residual risk** actually concentrated — by product, risk type, and control area?
- Are privileged access, vendor resilience, and oversight practices at the level expected for a critical payments rail?

This project simulates that role by:
- Treating **AuroraPay Debit and AuroraPay e‑Transfer** as distinct rails with different volume and fraud profiles.
- Focusing on five material product risk themes: **service outages, fraud and scams, technology & access, third‑party risk, and regulatory/oversight**.
- Using data to challenge whether the product is truly operating within appetite or simply “not obviously broken”.

For context on the fictional product and its environment, see:
- [Project Scenario](/docs/scenario.md)

[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

### Methodology

The analysis follows a simplified but realistic second‑line workflow:
- **Design the risk framework**
    - Define a **product‑aligned risk taxonomy** covering Operational, Fraud, Technology & Security, Third‑Party, and Regulatory & Oversight risk.
    - Build a **risk register** with risk IDs (R1–R12), appetite statements, and ownership.
    - Capture controls, incidents, and issues tied back to those risks.
- **Generate and prepare data (Python)**
    - Create a synthetic **transactions dataset** (~100k rows) with:
        - Product (Debit vs e‑Transfer), channel (POS, Online, Mobile), amount, status, and fraud flag.
    - Build CSVs for **risks, controls, incidents, and issues**.
    - Use [data_prep.ipynb](/notebooks/data_prep.ipynb) to perform light cleaning, derive date fields, and save processed datasets.
- **Calculate KRIs (Python / pandas)**
    - Use [risk_metrics.ipynb](/notebooks/risk_metrics.ipynb) to compute:
        - Transaction counts and volumes by product/channel.
        - Fraud rates by product.
        - Incident counts and downtime by risk and severity.
        - Open High/Critical issues by risk and risk category.
    - Export tidy tables to data/processed/ for use in Power BI.
- **Visualize and synthesize (Power BI + narrative)**
    - Build a Power BI report with:
        - **Overview page** for volumes, fraud exposure, and incidents.
        - **Risk & Issues page** showing open issues and a risk‑level KRI table.
    - Write [Product Risk Executive Summary](/reports/product_risk_executive_summary.md) to interpret the data from a second‑line perspective.

The risk taxonomy underlying this work is documented in:
- [Risk Taxonomy](/docs/risk_taxonomy.md)

[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

### Skills Demonstrated

This project is intentionally designed to showcase skills that map directly to a **Product Risk Lead** role in a payments environment.
- **Risk & Controls Design**
    - Building a **risk taxonomy, risk register,** and **control library** aligned to ERM and three‑lines‑of‑defence concepts.
    - Writing clear **risk appetite statements** and linking incidents/issues back to specific risks.
- **Python & Data Analytics (pandas)**
    - Synthetic data generation for transaction datasets.
    - Data preparation and feature derivation in [data_prep.ipynb](/notebooks/data_prep.ipynb).
    - KRI calculation in [risk_metrics.ipynb](/notebooks/risk_metrics.ipynb) (aggregations, join logic, grouping).
- **Power BI & Dashboarding**
    - Designing an **executive‑friendly** report that highlights:
        - Volumes, fraud rates, incidents, and open High/Critical issues.
        - Concentration of risk by product and risk category.
    - Using Power BI visuals (cards, bar charts, tables) to tell a risk story rather than just show data.
- **Executive‑level Risk Communication**
    - Writing an **executive risk summary** that:
        - Explains what is happening in business terms.
        - Connects metrics to **risk appetite and residual risk**.
        - Provides **credible second‑line challenge** and prioritized recommendations.

[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

### Results and Business Recommendations

Key findings from the analysis:
- **e‑Transfer is a smaller but more risk‑intensive rail**
    - e‑Transfer accounts for a smaller share of volume than Debit but exhibits a materially higher fraud rate, confirming it as the more risk‑dense rail.
    - This aligns with broader patterns where fast, irrevocable payments are disproportionately targeted by scams and account takeover.
- **Operational resilience is “stable but fragile”**
    - Outages and degradation incidents remain within the illustrative appetite in terms of count, but there are repeat patterns of latency and a concentration of incidents in specific components.
    - This suggests that underlying root causes are not fully addressed and that overall resilience could be tested by a cluster of events.
- **Privileged access and critical vendors are structural risk drivers**
    - High/Critical open issues are clustered around **privileged access** (legacy admin groups, delayed reviews) and vendor resilience (misaligned RTO/RPO for critical fraud analytics).
    - These structural weaknesses amplify the impact of any future operational or fraud event, even if current incident counts appear manageable.

From a second‑line perspective, the business should treat **fraud on e‑Transfer, privileged access, and critical vendor resilience** as priority focus areas, with time‑bound remediation plans and clear success criteria.

For the detailed narrative and recommendations, see:
- [Product Risk Executive Summary](/reports/product_risk_executive_summary.md)


[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

### Next Steps and Extensions

If this were a live environment, natural next steps would include:
- **Deepen fraud analytics on e‑Transfer**
    - Implement a formal **post‑incident tuning playbook** for fraud rules after scam spikes.
    - Explore more advanced detection (e.g., network‑based or behavioural scoring) to complement rules.
    - Integrate scam education directly into **high‑risk flows** (e.g., first‑time high‑value e‑Transfer sends).
- **Harden privileged access management**
    - Run a structured **privileged access remediation program** to:
        - Retire legacy admin groups and shared accounts.
        - Clarify ownership and usage of service accounts.
        - Embed quarterly challenge reviews with clear evidence of decision‑making.
- **Strengthen third‑party oversight**
    - Elevate key vendors into a **“critical services”** tier with:
        - RTO/RPO aligned to AuroraPay’s risk appetite.
        - Regular resilience testing and scenario exercises.
        - More robust control attestations and evidence.
- **Enhance oversight reporting and evidence**
    - Standardize **incident and change notifications** with explicit references to:
        - Risk appetite.
        - Residual risk assessment.
        - Status of remediation and open issues.
    - Extend the current dashboards into a **repeatable reporting pack** for MRC/BRC‑style committees.

**Limitations**
- All data in this project is **synthetic** and designed for learning and demonstration only.
- The ecosystem, participants, and regulatory requirements are **simplified** relative to a live national payments rail.
- The focus is intentionally narrow (five risk themes) to allow for depth rather than exhaustive coverage.

[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

### Project Files

- [data/raw/](/data/raw/) – Synthetic source datasets (transactions, risks, controls, incidents, issues).
- [data/processed/](/data/processed/) – Cleaned datasets and KRI tables used for analysis and Power BI.
- [notebooks/data_prep.ipynb](/notebooks/data_prep.ipynb) – Data loading, cleaning, and basic descriptive analysis.
- [notebooks/risk_metrics.ipynb](/notebooks/risk_metrics.ipynb) – KRI calculations and risk‑level summaries.
- [src/](/src/) – Python scripts (e.g., synthetic data generation).
- [powerbi/AuroraPayProductRiskCaseStudy](/powerbi/AuroraPayProductRiskCaseStudy.pbix) - Power BI report.
- [powerbi/screenshots](/powerbi/screenshots/) – PNG exports of key report pages.
- [docs/scenario.md](/docs/scenario.md) – AuroraPay product context and design assumptions.
- [docs/risk_taxonomy.md](/docs/risk_taxonomy.md) – Product risk taxonomy used across the project.
- [reports/product_risk_executive_summary.md](/reports/product_risk_executive_summary.md) – Executive risk paper summarizing findings and recommendations.

[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

### How to Run

- **Prerequisites**
    - Python 3.10+
    - Recommended: a virtual environment tool (e.g., venv or conda)
    - Power BI Desktop (for viewing the .pbix report)

1. Clone the repository
```bash
git clone https://github.com/<your-username>/aurorapay-product-risk-case-study.git
cd aurorapay-product-risk-case-study
```

2. Set up the Python environment
If you use **venv**:
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the notebooks
- Start Jupyter:
```bash
jupyter notebook
```
- Open and run the notebooks in order:
    - [notebooks/data_prep.ipynb](/notebooks/data_prep.ipynb)
        - Loads raw CSVs from [data/raw/](/data/raw/), performs light cleaning, and saves processed datasets to [data/processed/](/data/processed/).
    - [notebooks/risk_metrics.ipynb](/notebooks/risk_metrics.ipynb)
        - Loads processed data, calculates KRIs (transaction volumes, fraud rates, incidents, issues), and exports summary tables to [data/processed/](/data/processed/) for Power BI.

You can re‑generate the synthetic transactions dataset by re‑running the data generation cell or script referenced in [data_prep.ipynb](/notebooks/data_prep.ipynb) (or [src/generate_transactions.py](/src/generate_transactions.py) if you split it out).

4. Open the Power BI report
- Launch Power BI Desktop.
- Open:
```text
powerbi/aurorapay_product_risk.pbix
```
- The report should automatically connect to the CSVs under data/processed/. If you change file locations, update the data source paths in Power BI.

5. Explore key artifacts
- Scenario and context: [docs/scenario.md](/docs/scenario.md)
- Risk taxonomy: [docs/risk_taxonomy.md](/docs/risk_taxonomy.md)
- Executive risk paper: [reports/product_risk_executive_summary.md](/reports/product_risk_executive_summary.md)
- Dashboard screenshots (if you don’t have Power BI): [powerbi/screenshots/](/powerbi/screenshots/)

[Back to Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

## License

MIT License

Copyright (c) [2026] [Prasanna Sriram]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back to the Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)

---

## Author Info

- Github - [Github Profile](https://github.com/prasanna-sriram)
- LinkedIn - [Prasanna Sriram](https://www.linkedin.com/in/prasanna-sriram/)
- Tableau - [Tableau Public Profile](https://public.tableau.com/app/profile/prasanna.sriram.ps)

[Back to the Top](#aurorapay-product-risk-analytics-for-realtime-payments-erm-operational-risk-fraud-access-management)