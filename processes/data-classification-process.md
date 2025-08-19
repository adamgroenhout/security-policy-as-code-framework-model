---
creation_date: 2025-08-16
origin: "To be determined"
origin_details: "To be determined"
process_id: ds-proc-001
title: "Data Classification Process"
standard_id: ds-std-001
---

# 1. Overview
This document provides the step-by-step process for classifying a new data asset in accordance with the Data Classification Standard.

# 2. Prerequisites
*   The individual performing the classification must have completed the mandatory annual security awareness training.
*   The individual must have access to the `data-classification-standard.md` for reference.
*   The data asset must have an identified Data Owner.

# 3. Process Steps

1.  **Initiation:** The process is initiated when a new data asset (e.g., a new database, a new application, a new shared folder) is created.
2.  **Identify Data Owner:** The manager of the team creating the asset is responsible for assigning a Data Owner. The Data Owner is the senior individual ultimately responsible for the asset.
3.  **Analyze Data Content:** The Data Owner or their delegate (e.g., a technical lead) must analyze the data that will be stored in the asset.
    *   *Action:* Review the data schema, sample data, and intended use.
    *   *Consider:* Does the data contain PII, financial information, health information, intellectual property, or other sensitive information?
4.  **Determine Classification:** Based on the analysis, the Data Owner must determine the highest appropriate classification level by consulting the `data-classification-standard.md`. The classification of the asset must match the highest classification of any data element within it.
5.  **Apply Classification Label:** The Data Owner must ensure a label indicating the classification level is applied to the asset.
    *   *Examples:* Applying a "Classification: Confidential" tag in the cloud console, adding a `CLASSIFICATION` column to a database schema, or ensuring the application's UI displays the classification.
6.  **Document and Review:** The classification decision, including the justification, must be recorded in the corporate Asset Inventory system. The classification should be reviewed annually by the Data Owner.

# 4. Expected Outcomes
*   All new data assets are classified within 30 days of creation.
*   The classification is recorded in the Asset Inventory system.
*   Appropriate security controls can be applied based on the assigned classification level.
