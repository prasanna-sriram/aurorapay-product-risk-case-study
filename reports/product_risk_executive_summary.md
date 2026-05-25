# Executive Risk Summary

---

### Table of Contents

- [Purpose and Scope](#purpose-and-scope)
- [Snapshot of AuroraPay and Key Metrics](#snapshot-of-aurorapay-and-key-metrics)
- [Thematic Assessment by Risk Area](#thematic-assessment-by-risk-area)
    - [Service Outages and Instability](#service-outages-and-instability)
    - [Fraud and Scams](#fraud-and-scams)
    - [Technology and Access](#technology-and-access)
    - [Third Party and Ecosystem Risk](#thirdparty-and-ecosystem-risk)
    - [Regulatory and Oversight](#regulatory-and-oversight)
- [Overall Residual Risk Assessment](#overall-residual-risk-assessment)
- [Prioritized Actions and Recommendations](#prioritized-actions-and-recommendations)

---

### Purpose and Scope

This summary provides a second‑line view of AuroraPay’s product risk posture for the **Q1 2026 synthetic period**, focusing on operational resilience, fraud and scams, technology and access controls, third‑party dependencies, and regulatory/oversight risk. It synthesizes transaction data, incidents, controls, and issues into key risk indicators (KRIs) and highlights areas where residual risk approaches or exceeds the illustrative risk appetite.

[Back to Top](#executive-risk-summary)

---

### Snapshot of AuroraPay and Key Metrics

Over the *Q1 2026 period*, AuroraPay processed approximately **100,000 transactions** representing **CAD 2.76M in total volume** across Debit and e‑Transfer rails. Debit carried the majority of volume, while e‑Transfer remained a smaller but more risk‑dense rail with a materially higher fraud rate than Debit.

Across the same period, we observed **8 recorded incidents** (of which **6 were High/Critical**) and **8 open High/Critical issues** concentrated in a small number of risk areas.

- **Debit: 59.8K transactions, CAD 1.65M volume, fraud rate 0.052%.**
- **e‑Transfer: 40.2K transactions, CAD 1.11M volume, fraud rate 0.289%.**

This means e‑Transfer accounts for roughly 40% of volume but over five times the fraud rate of Debit, reinforcing it as the more risk‑intensive rail.

[Back to Top](#executive-risk-summary)

---

### Thematic Assessment by Risk Area

#### Service outages and instability

**Observation:** AuroraPay experienced one Critical nationwide e‑Transfer outage and several High‑severity degradation incidents, resulting in a total of **152 minutes of disruption**, primarily during peak usage windows. While the number of major incidents remains within the illustrative appetite of ≤1 per quarter, repeat latency issues linked to similar patterns suggest that underlying root causes are not fully resolved.

**Second‑line view:** From a second‑line perspective, operational resilience is stable but fragile: headline metrics remain within appetite, yet the concentration of incidents in a small set of components, combined with an open High‑severity issue on repeat root causes, indicates elevated residual risk. We recommend prioritizing structural remediation for R12 rather than treating each incident as an isolated event.

#### Fraud and scams

**Observation:** **e‑Transfer exhibits a fraud rate of approximately 0.289% versus 0.052% on Debit**, confirming it as the more fraud‑intensive rail despite its smaller share of overall volume. Fraud losses remain within the illustrative appetite in aggregate, but the January–February scam campaign and subsequent account takeover cluster show that new patterns can emerge quickly and exploit gaps in rules tuning and customer education.

**Second‑line view:** Fraud controls are directionally effective but reactive. The open High‑severity issue on post‑incident rules tuning, combined with incomplete integration of scam education into high‑risk flows, suggests that residual fraud risk on e‑Transfer is at the upper end of appetite. We recommend formalizing a “playbook” for rapid tuning after fraud spikes and making scam education a mandatory part of specific transaction journeys.

Given AuroraPay’s role as critical retail infrastructure, e‑Transfer fraud should be treated as a focus area for 2026, with clear targets to bring loss rates closer to Debit over time.

#### Technology and Access 

**Observation:** Most Technology & Security risks have limited incident history in the period, but privileged access and monitoring remain structural weaknesses. We have two High/Critical open issues related to legacy admin groups and delayed privileged access reviews, alongside partial gaps in centralized security logging. While no confirmed misuse has been detected, these weaknesses amplify the potential impact of any operational or fraud event.

**Second‑line view:** From a second‑line standpoint, privileged access management is not yet at the level expected for a critical payments rail. Residual risk on R5/R11 should be treated as elevated until all legacy admin paths are retired, recertifications are consistently challenged, and ownership of service accounts is fully clarified. We recommend treating privileged access remediation as a time‑bound program rather than a series of tactical fixes.

Privileged access should be considered one of the top structural risks for AuroraPay until the current issues are closed and a sustainable review cadence is embedded.

#### Third‑party and Ecosystem Risk

**Observation:** The fraud analytics vendor outage in January forced AuroraPay into fallback modes with reduced detection capability for approximately **45 minutes**. While direct loss was limited and service was restored within an hour, the incident highlighted misalignment between contracted RTO/RPO and the effective criticality of the service to AuroraPay’s fraud posture.

**Second‑line view:** Residual third‑party risk is higher than implied by the current contractual and oversight framework. Critical vendors that influence fraud detection or transaction processing should be governed under RTO/RPO and control expectations consistent with their role in AuroraPay’s end‑to‑end risk profile. We recommend elevating these providers into a “critical services” tier with enhanced due diligence, testing, and resilience expectations.

#### Regulatory and Oversight

**Observation:** A late and incomplete notification related to the February e‑Transfer outage demonstrated that documentation of risk appetite alignment, residual risk assessment, and remediation effectiveness is not yet embedded in incident reporting.

**Second‑line view:** While the incident itself was contained, the oversight angle exposed weaknesses in how risk decisions and remediation are evidenced. For a rail of AuroraPay’s systemic importance, the ability to clearly articulate “what happened, how it relates to appetite, and why we are comfortable with residual risk” is critical. We recommend standardizing an incident reporting template that explicitly covers linkage to risk appetite and residual risk.

[Back to Top](#executive-risk-summary)

---

### Overall Residual Risk Assessment

Overall, AuroraPay’s risk profile for the period remains broadly within the illustrative appetite on headline metrics: volumes and fraud losses are stable, the number of major outages is limited, and there were no confirmed security breaches. However, residual risk is elevated in specific areas — particularly fraud on e‑Transfer, privileged access, and critical vendor resilience — where High/Critical issues remain open and where the combination of events could push us beyond tolerance even if individual metrics remain acceptable.

From a second‑line perspective, these areas warrant continued heightened attention and structured remediation programs rather than incremental fixes.

[Back to Top](#executive-risk-summary)

---

### Prioritized Actions and Recommendations

- **Fraud and e‑Transfer:** Implement a formal post‑incident tuning playbook and embed scam education into high‑risk e‑Transfer flows (e.g., first‑time high‑value sends).
- **Privileged access:** Run a time‑bound privileged access remediation program to retire legacy admin groups, clarify service account ownership, and enforce quarterly challenge reviews.
- **Critical vendor resilience:** Elevate key vendors into a critical tier with aligned RTO/RPO and test periodic failover / fallback scenarios.
- **Regulatory evidence:** Standardize incident reports and risk papers to explicitly reference risk appetite, residual risk assessment, and remediation effectiveness.

[Back to Top](#executive-risk-summary)