---
policy_id: ns-001
title: Network Security Policy
owner: "@github/network-engineering"
sme: "network.engineering@example.com"
next_annual_certification_date: 2025-08-10
---

# 1. Overview
This policy defines the requirements for securing the company's network infrastructure against threats and unauthorized access. Its goal is to protect the confidentiality, integrity, and availability of data traversing the network.

# 2. Scope
This policy applies to all network infrastructure, both physical and virtual, including but not limited to routers, switches, firewalls, wireless access points, VPNs, and cloud networking components.

# 3. Policy Statements

*   **PS-1: Network Segmentation:** The corporate network must be segmented into logical security zones based on data sensitivity and system criticality. Traffic between zones must be restricted by firewalls on a default-deny basis.
*   **PS-2: Firewall Management:** All firewalls must be configured according to the `firewall-rule-standard.md`. All changes to firewall rules must follow the `firewall-rule-request-process.md`.
*   **PS-3: Intrusion Detection and Prevention:** Intrusion Detection and Prevention Systems (IDPS) must be deployed at key network boundaries to monitor for, detect, and block malicious traffic. All alerts must be sent to the Security Operations Center (SOC) for analysis.
*   **PS-4: Wireless Security:** All corporate wireless networks must be secured with strong encryption (WPA2/WPA3). A separate, segregated guest network must be provided for visitors, with no access to the internal corporate network.
*   **PS-5: Network Monitoring:** Network traffic must be logged and monitored to detect anomalies and potential security incidents. Logs must be retained for a minimum of 90 days.

# 4. Roles and Responsibilities

*   **Network Engineering Team:** Responsible for the design, implementation, and maintenance of the network infrastructure and its security controls.
*   **Security Operations Center (SOC):** Responsible for monitoring network activity, analyzing IDPS alerts, and responding to potential incidents.
*   **All Employees:** Responsible for complying with the wireless security requirements and not introducing unauthorized network devices.

# 5. Compliance

*   **Measurement:** Compliance with this policy will be measured through regular network vulnerability scans, penetration testing, and audits of firewall rulebases.
*   **Exceptions:** Any exception to this policy must be formally documented and approved by the Head of Network Engineering and the CISO. All exceptions require a documented risk assessment and will be reviewed annually.
*   **Enforcement:** Unauthorized changes to network configurations or violation of this policy may result in disciplinary action.

## Applicable Controls

* **ISO 27001**: A.13.1, A.13.2
* **SOC 2**: CC3.2
* **NIST CSF**: PR.PT-4
