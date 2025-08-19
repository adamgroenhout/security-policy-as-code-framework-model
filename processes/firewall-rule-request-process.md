---
process_id: ns-proc-001
title: "Firewall Rule Request Process"
policy_id: ns-001
---

# 1. Overview
This document provides the step-by-step process for requesting, approving, implementing, and reviewing a firewall rule change. This process is designed to ensure that all changes are authorized, documented, and compliant with the Firewall Rule Standard.

# 2. Prerequisites
*   The requestor must have a clear, documented business or technical justification for the rule change.
*   The requestor must know the specific source IPs, destination IPs, and destination ports/protocols required.

# 3. Process Steps

1.  **Initiate Request:** The requestor opens a "Firewall Rule Request" ticket in Jira.
    *   *Action:* The requestor must complete all fields in the form, providing detailed and accurate information. Vague requests (e.g., "open port 443 for server X") will be rejected.
2.  **Manager Approval:** The Jira workflow automatically routes the ticket to the requestor's direct manager for approval.
    *   *Action:* The manager reviews the business justification. If approved, the ticket proceeds. If rejected, the ticket is closed.
    *   *SLA:* 2 business days.
3.  **Technical Review:** The ticket is assigned to the Network Engineering team queue.
    *   *Action:* A network engineer reviews the request against the `firewall-rule-standard.md`. They check for specificity, rule shadowing, and overall security impact. The engineer may ask for clarification or suggest alternatives.
    *   *SLA:* 3 business days.
4.  **Implementation:** If the technical review is approved, the network engineer schedules and implements the change during the next available change window.
    *   *Action:* The engineer applies the rule change and performs post-implementation testing to ensure functionality and verify that only the intended access was granted.
5.  **Notification:** The requestor is notified of the successful implementation via the Jira ticket. The ticket is then resolved.

# 4. Expected Outcomes
*   All firewall rule changes are properly authorized and documented, creating a clear audit trail.
*   Firewall rules are implemented in a way that adheres to the principle of least privilege.
*   The requestor is kept informed of the status of their request throughout the process.
