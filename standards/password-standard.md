---
creation_date: 2025-08-16
origin: "To be determined"
origin_details: "To be determined"
standard_id: ac-std-001
title: "Password Standard"
policy_id: ac-001
---

# 1. Overview
This standard supports the Access Control Policy by defining the minimum mandatory requirements for all user and system account passwords. Its purpose is to reduce the risk of unauthorized access through compromised credentials.

# 2. Scope
This standard applies to all passwords used to authenticate to any company-owned or managed system, application, or service, for all user types including employees, contractors, customers, and system accounts.

# 3. Standard Requirements

## 3.1. User Passwords
All passwords for interactive user accounts must meet the following criteria:
*   **Minimum Length:** 14 characters.
*   **Complexity:** Must contain characters from at least three of the following four categories:
    *   Uppercase letters (A-Z)
    *   Lowercase letters (a-z)
    *   Numbers (0-9)
    *   Special characters (`~!@#$%^&*_-+=`|\\(){}[]:;"'<>,.?/`)
*   **History:** Users may not reuse any of their last 12 passwords.
*   **Expiration:** Passwords must be changed at least every 90 days.
*   **Storage:** Passwords must be stored in a hashed format using a modern, industry-standard algorithm (e.g., Argon2, bcrypt) with a unique salt per user.

## 3.2. System and Service Account Passwords
*   Passwords for system or service accounts must be at least 24 characters long and randomly generated.
*   These passwords should be stored securely in an approved vault and rotated at least annually, or immediately upon the departure of any personnel with access to them.

## 3.3. Multi-Factor Authentication (MFA)
MFA must be enabled on all user accounts where it is supported, especially for access to Restricted or Confidential data, and for all remote access to the corporate network.

# 4. Enforcement
Compliance with this standard will be enforced at a technical level by the respective systems and applications. The Security Engineering team will periodically audit systems to ensure they are configured to enforce these requirements. Accounts found to be non-compliant may be disabled until they are brought into compliance.
