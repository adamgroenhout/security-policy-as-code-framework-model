---
standard_id: ds-std-001
title: "Data Classification Standard"
policy_id: ds-001
creation_date: 2025-08-16
origin: "To be determined"
origin_details: "To be determined"
---

# 1. Overview
This standard operationalizes the Data Security Policy by defining the official data classification levels. It provides a framework for employees and data owners to categorize data based on its sensitivity, criticality, and legal requirements.

# 2. Scope
This standard applies to all company and customer data, regardless of its format or location. All new and existing data assets must be classified in accordance with this standard.

# 3. Standard Requirements

## 3.1. Classification Levels

*   **Restricted:** Data with the highest sensitivity. Unauthorized disclosure could cause catastrophic harm to the business, its customers, or partners.
    *   *Examples:* Customer financial data, authentication secrets (passwords, API keys), patient health information (PHI), source code for critical applications.
    *   *Minimum Controls:* Strong encryption at rest and in transit, strict need-to-know access control, extensive logging and monitoring, data loss prevention (DLP) enabled.

*   **Confidential:** Sensitive data intended for internal use only by a limited, authorized audience. Unauthorized disclosure could have a significant negative impact on the business.
    *   *Examples:* Business strategy documents, employee PII, internal financial reports, legal documents.
    *   *Minimum Controls:* Encryption at rest and in transit, role-based access control, standard logging.

*   **Internal:** Data intended for all internal employees but not for public disclosure. Unauthorized disclosure could cause minor operational disruption or reputational harm.
    *   *Examples:* Internal wikis, general team communications, company announcements, non-sensitive operational data.
    *   *Minimum Controls:* Access restricted to internal network/users, standard logging.

*   **Public:** Data that is approved for public release.
    *   *Examples:* Marketing materials, public website content, press releases, job postings.
    *   *Minimum Controls:* No confidentiality controls required, but integrity controls should be in place to prevent unauthorized modification.

## 3.2. Data Labeling
All data assets, where technically feasible, must be labeled with their classification level. This can be done via metadata tags, document headers/footers, or within the application interface.

# 4. Enforcement
Compliance with this standard will be verified through periodic audits and data discovery scans. Failure to properly classify data may result in the data being assigned the highest possible classification level by default and may lead to disciplinary action for the responsible data owner.
