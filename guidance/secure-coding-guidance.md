---
guidance_id: vm-guide-001
title: "Secure Coding Guidance"
policy_id: vm-001
---

# Secure Coding Guidance

This document provides non-mandatory guidance and best practices for developers to help prevent common security vulnerabilities in software. Following this guidance is highly recommended to improve the security posture of our applications.

## Key Recommendations

*   **Validate All Input:** Treat all input from users or external systems as untrusted. Always validate, sanitize, and encode input to prevent injection attacks (e.g., SQL Injection, Cross-Site Scripting).
*   **Use Parameterized Queries:** Never construct SQL queries using string concatenation. Use prepared statements or parameterized queries to prevent SQL injection.
*   **Implement Strong Authentication and Session Management:** Use a well-vetted library for authentication. Do not roll your own. Ensure session tokens are generated with high entropy and are invalidated upon logout.
*   **Practice Defense in Depth:** Do not rely on a single security control. Layer multiple defenses (e.g., input validation, access control, logging) to provide redundancy.
*   **Keep Dependencies Updated:** Regularly check for and update third-party libraries to patch known vulnerabilities. Use tools like Dependabot or Snyk to automate this.
