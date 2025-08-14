---
guidance_id: vm-guide-001
title: "Secure Coding Guidance"
policy_id: vm-001
---

# 1. Overview
This document provides non-mandatory guidance and best practices for developers to help prevent common security vulnerabilities in software. Following this guidance is highly recommended to improve the security posture of our applications and reduce the number of vulnerabilities that need to be remediated.

# 2. Key Recommendations

## 2.1. Validate All Input
Treat all input from users or external systems as untrusted. Always validate, sanitize, and encode input to prevent injection attacks.
*   **Example (SQL Injection):** Never use string concatenation to build SQL queries. Use parameterized queries (prepared statements) instead.
*   **Example (Cross-Site Scripting - XSS):** HTML-encode all user-supplied content before rendering it in a web page to prevent malicious scripts from executing.

## 2.2. Implement Strong Authentication and Session Management
*   **Guidance:** Use a well-vetted, industry-standard library or framework for authentication (e.g., Passport.js, Spring Security). Do not build your own authentication logic.
*   **Guidance:** Ensure session tokens are generated with high entropy and are invalidated on the server-side upon logout. Store session tokens securely (e.g., in an `HttpOnly` cookie).

## 2.3. Practice Secure Access Control
*   **Guidance:** Enforce authorization checks on the server-side for every request. Do not rely on the client-side UI to enforce access control, as it can be easily bypassed.
*   **Example (Insecure Direct Object Reference - IDOR):** Instead of `GET /api/documents/123`, use a URL that is not guessable or ensure that the logged-in user is actually authorized to view document `123` before returning it.

## 2.4. Keep Dependencies Updated
*   **Guidance:** Regularly check for and update third-party libraries to patch known vulnerabilities.
*   **Tools:** Use tools like GitHub's Dependabot, Snyk, or OWASP Dependency-Check to automate the detection of vulnerable dependencies in your projects.

# 3. Helpful Resources
*   **OWASP Top 10:** A standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications. [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
*   **OWASP Cheat Sheet Series:** A collection of concise cheat sheets on specific security topics, providing actionable guidance. [https://cheatsheetseries.owasp.org/](https://cheatsheetseries.owasp.org/)
