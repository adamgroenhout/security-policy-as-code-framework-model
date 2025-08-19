---
policy_id: ac-001
title: Access Control Policy
owner: "@github/security-engineering-team"
sme: "security.engineering@example.com"
next_annual_certification_date: 2025-08-10
creation_date: 2025-08-16
origin: "To be determined"
origin_details: "To be determined"
---

# 1. Overview
This policy establishes the requirements for controlling access to company systems, data, and physical facilities to protect against unauthorized access, modification, or destruction.

# 2. Scope
This policy applies to all employees, contractors, and third parties, and it covers all company assets, including networks, systems, applications, databases, and physical locations.

# 3. Policy Statements

*   **PS-1: Principle of Least Privilege:** Access shall be granted based on the principle of least privilege, meaning users are given only the minimum level of access necessary to perform their assigned job responsibilities.
*   **PS-2: Unique User Identity:** All users must be assigned a unique user ID. The use of shared or group accounts is strictly prohibited for any system that can be traced back to an individual's actions.
*   **PS-3: Access Reviews:** User access rights to all systems and applications must be reviewed on a quarterly basis by the asset owner or the user's manager. Any access that is no longer required must be revoked in a timely manner.
*   **PS-4: Password Management:** All passwords must adhere to the requirements defined in the `password-standard.md`.
*   **PS-5: Remote Access:** Remote access to the corporate network must be secured using company-approved, multi-factor authentication (MFA) methods.

# 4. Roles and Responsibilities

*   **Security Engineering Team:** Responsible for implementing and maintaining access control systems and tools.
*   **Asset Owners:** Responsible for defining and approving access levels for their respective systems and applications.
*   **Managers:** Responsible for reviewing their direct reports' access rights on a quarterly basis and requesting changes as needed.
*   **All Employees:** Responsible for safeguarding their access credentials and reporting any suspected compromises.

# 5. Compliance

*   **Measurement:** Compliance with this policy will be verified through regular access reviews, system audits, and penetration testing.
*   **Exceptions:** Any exception to this policy must be formally documented and approved by the Security Engineering team and the CISO. All exceptions require a documented risk assessment and will be reviewed annually.
*   **Enforcement:** Unauthorized access or sharing of credentials will result in disciplinary action, up to and including termination of employment.

## Applicable Controls

* **ISO 27001**: A.9.1, A.9.2, A.9.4
* **SOC 2**: CC6.1, CC6.2, CC6.3
* **NIST CSF**: PR.AC-1, PR.AC-3, PR.AC-4
