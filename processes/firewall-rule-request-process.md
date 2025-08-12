---
process_id: ns-proc-001
title: "Firewall Rule Request Process"
standard_id: ns-std-001
---

# Firewall Rule Request Process

This document provides the step-by-step process for requesting a new firewall rule or modifying an existing one, in accordance with the Firewall Rule Standard.

## Process Steps

1.  **Identify the Need:** Clearly define the business or technical need for the firewall rule. This includes identifying the source and destination systems and the specific ports required.
2.  **Fill out the Request Form:** Open a ticket using the "Firewall Rule Request" template in Jira. Provide all required information, including:
    *   Business Justification
    *   Source IP(s)
    *   Destination IP(s)
    *   Destination Port(s) and Protocol(s) (TCP/UDP)
    *   Requested duration (permanent or temporary with an expiration date)
3.  **Submit for Approval:** The ticket will be automatically routed to the requestor's manager for initial approval.
4.  **Network Team Review:** Once approved by the manager, the ticket is assigned to the Network Engineering team for technical review. The team will verify that the request complies with the Firewall Rule Standard.
5.  **Implementation:** If the technical review is successful, the Network Engineering team will implement the rule change.
6.  **Notification:** The requestor will be notified via the Jira ticket once the rule has been implemented and verified.
