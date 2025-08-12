---
standard_id: ns-std-001
title: "Firewall Rule Standard"
policy_id: ns-001
---

# Firewall Rule Standard

This standard supports the Network Security Policy by defining the requirements for all firewall rules on network and host-based firewalls.

## Rule Requirements

All firewall rules must adhere to the principle of least privilege.
*   **Default Deny:** All firewalls must operate on a default-deny basis, where all traffic is blocked unless explicitly allowed by a rule.
*   **Specificity:** Rules must be as specific as possible, limiting access to only the required source IPs, destination IPs, and ports. The use of "any" is prohibited unless explicitly justified and approved.
*   **Documentation:** Every rule must have a clear business justification, owner, and creation date documented in the firewall management interface.
*   **Review:** All firewall rules must be reviewed on an annual basis to ensure they are still required and correctly configured. Temporary rules must have an expiration date.
