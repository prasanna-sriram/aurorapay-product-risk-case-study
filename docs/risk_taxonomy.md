# AuroraPay Product Risk Taxonomy

This document defines the product‑aligned risk taxonomy used for the AuroraPay case study. It provides a consistent set of categories and sub‑categories for classifying risks, controls, issues, and incidents across AuroraPay Debit and AuroraPay e‑Transfer.

The taxonomy is designed to be simple enough for product teams to use while still aligning to common enterprise risk management practices and the three lines of defense model.

---

### Table of Contents

- [Operational Risk](#1-operational-risk)
- [Fraud Risk](#2-fraud-risk)
- [Technology and Security Risk](#3-technology-and-security-risk)
- [Third-Party and Ecosystem Risk](#4-thirdparty-and-ecosystem-risk)
- [Regulatory and Oversight Risk](#5-regulatory-and-oversight-risk)
- [Reputational and Franchise Risk](#6-reputational-and-franchise-risk)
- [Usage in this project](#7-usage-in-this-project)

[Back to top](#aurorapay-product-risk-taxonomy)

---

### 1. Operational Risk
Operational risk covers failures of processes, people, or internal systems that impact the availability, reliability, or quality of AuroraPay services.

Key sub‑categories:
- **Service Availability & Stability**
Risks related to outages, degraded performance, capacity shortfalls, and failed changes that materially impact the ability of participants and end users to send and receive payments.
- **Process & Execution**
Risks arising from manual errors, incomplete procedures, or inconsistent execution of operational tasks (e.g., reconciliation, settlement processing, incident handling).
- **Change & Release Management**
Risks associated with inadequate testing, rushed deployments, or poorly controlled changes that introduce defects into production environments.

In this case study, service availability and stability is a primary focus theme, given AuroraPay’s role as critical payments infrastructure.

[Back to top](#aurorapay-product-risk-taxonomy)

---

### 2. Fraud Risk
Fraud risk covers intentional misuse of AuroraPay products and channels for financial gain, typically involving deception, compromised accounts, or abuse of product features.

Key sub‑categories:
- **Customer‑Facing Fraud & Scams**
Social‑engineering scams, invoice fraud, and other schemes where end users are tricked into authorizing payments they did not intend.
- **Account Takeover & Credential Abuse**
Fraud resulting from compromised credentials, devices, or access tokens that allow unauthorized parties to initiate payments.
- **Internal or Insider‑Enabled Fraud**
Fraud facilitated by excessive access, collusion, or override of controls by insiders or ecosystem partners.

This case study primarily models customer‑facing fraud and account takeover, with fraud loss measured relative to transaction volume and compared against a defined risk appetite.

[Back to top](#aurorapay-product-risk-taxonomy)

---

### 3. Technology and Security Risk
Technology & security risk covers failures or weaknesses in the design, implementation, or operation of AuroraPay’s technology stack that could compromise availability, integrity, or confidentiality.

Key sub‑categories:
- **Access Control & Privileged Access**
Risks related to over‑privileged accounts, shared credentials, inadequate segregation of duties, or weak authentication protecting core systems and tools.
- **Security Monitoring & Incident Detection**
Risks stemming from insufficient logging, monitoring, alerting, or incident response capabilities that could delay detection or containment of security events.
- **Data Protection & Privacy**
Risks involving unauthorized access to, or disclosure of, sensitive transaction data or personal information, including failures in encryption, key management, or data handling processes.

The case study focuses on access control and monitoring weaknesses in critical AuroraPay systems that could amplify the impact of fraud, outages, or data breaches.

[Back to top](#aurorapay-product-risk-taxonomy)

---

### 4. Third‑Party and Ecosystem Risk
Third‑party & ecosystem risk covers dependencies on external service providers and ecosystem partners whose failures can affect AuroraPay’s ability to deliver services or maintain control effectiveness.

Key sub‑categories:
- **Critical Service Providers**
Outsourced services such as fraud analytics, connectivity, infrastructure, or shared platforms whose outages or control failures directly impact AuroraPay operations.
- **Data & Integration Risk**
Risks arising from integration defects, data quality issues, or interface failures between AuroraPay and participants, vendors, or partners.
- **Concentration & Sub‑Outsourcing**
Risks from excessive reliance on a small number of providers or layered outsourcing chains that are difficult to oversee.

In this case study, critical service provider outages and weaknesses in vendor‑managed controls are modeled as key contributors to service availability and security risk.

[Back to top](#aurorapay-product-risk-taxonomy)

---

### 5. Regulatory and Oversight Risk
Regulatory & oversight risk covers failures to meet expectations set by regulators and oversight bodies regarding operational resilience, risk management, and transparency.

Key sub‑categories:
- **Operational Resilience & Standards Compliance**
Risks of non‑compliance with requirements and expectations related to uptime, recovery objectives, and preparedness for disruptive events.
- **Incident & Change Notifications**
Risks that material incidents, changes, or control weaknesses are not reported to oversight bodies accurately, consistently, or within required timeframes.
- **Documentation & Evidence**
Risks that risk decisions, control assessments, and remediation actions are not sufficiently documented to demonstrate alignment with risk appetite and standards.

The case study models regulatory and oversight risk primarily through the lens of major incidents, unresolved issues, and their implications for required notifications and supervisory confidence.

[Back to top](#aurorapay-product-risk-taxonomy)

---

### 6. Reputational and Franchise Risk

Reputational risk reflects the potential for adverse public, participant, or stakeholder perception to erode trust in AuroraPay, even when direct financial losses are limited.

Rather than creating separate incidents for reputational risk, **this case study treats it as cross‑cutting**, recognizing that:
- Extended outages, highly publicized fraud cases, or repeated control failures can rapidly damage trust.
- Reputational impact often arises from the combination of operational, fraud, technology, third‑party, and regulatory events.

Reputational considerations are surfaced qualitatively in the executive risk summary whenever patterns of incidents and control gaps suggest a potential erosion of trust.

[Back to top](#aurorapay-product-risk-taxonomy)

---

### 7. Usage in this project

In this project:
- Each risk in the risk register is assigned a primary category from this taxonomy.
- Incidents, issues, and controls are tagged to the category (and where helpful, sub‑category) that best reflects their primary risk driver.
- Metrics and dashboards summarize exposure and trends by these categories, enabling a product‑level view of risk that aligns with enterprise frameworks but remains understandable to product and technology stakeholders.

[Back to top](#aurorapay-product-risk-taxonomy)