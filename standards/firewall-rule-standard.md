---
standard_id: ns-std-001
title: "Firewall Rule Standard"
policy_id: ns-001
creation_date: 2025-08-16
origin: "To be determined"
origin_details: "To be determined"
---

# 1. Overview
This standard supports the Network Security Policy by defining the mandatory requirements for the configuration and management of all firewall rules. The objective is to ensure that only authorized traffic is allowed to traverse network boundaries.

# 2. Scope
This standard applies to all network and host-based firewalls deployed within the corporate environment, including cloud security groups and network access control lists (ACLs).

# 3. Standard Requirements

## 3.1. Rule Configuration
All firewall rules must adhere to the principle of least privilege.
*   **Default Deny:** All firewalls must be configured with an implicit or explicit "deny all" rule at the end of the rulebase. All allowed traffic must be explicitly permitted.
*   **Specificity:** Rules must be as specific as possible.
    *   **Source/Destination:** Source and destination fields must be restricted to specific IP addresses or approved, well-defined groups. The use of "any" or "0.0.0.0/0" is prohibited unless there is a documented and approved business justification.
    *   **Ports/Protocols:** Port and protocol fields must be restricted to only those required for the application to function.
*   **No Shadowed Rules:** Rulebases must be configured to avoid "shadowed" rules, where a rule is rendered ineffective by a preceding rule.
*   **Logging:** All traffic that is blocked by the firewall must be logged. All traffic that is allowed through critical firewall gateways (e.g., internet-facing) must also be logged.

## 3.2. Rule Management
*   **Documentation:** Every rule must have a clear business justification, an owner (individual or team), and a creation date documented in the firewall management platform.
*   **Review:** All firewall rules must be reviewed on an annual basis by the rule owner to ensure they are still required and correctly configured. Temporary rules must have an expiration date configured and must be automatically removed upon expiration.
*   **Change Management:** All changes to firewall rules must follow the `firewall-rule-request-process.md`.

# 4. Enforcement
The Network Engineering team is responsible for enforcing this standard. Automated tools will be used to audit firewall rulebases for compliance with these requirements. Any non-compliant rules will be flagged for immediate review and remediation.
