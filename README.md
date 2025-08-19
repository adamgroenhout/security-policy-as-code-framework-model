_ _
                      ___  ___  ___ _   _ _ __(_) |_ _   _
                     / __|/ _ \/ __| | | | '__| | __| | | |
                     \__ \  __/ (__| |_| | |  | | |_| |_| |
                     |___/\___|\___|\__,_|_|  |_|\__|\__, |
                                                     |___/

                      _ _                                        _
         _ __   ___ | (_) ___ _   _    __ _ ___    ___ ___   __| | ___
        | '_ \ / _ \| | |/ __| | | |  / _` / __|  / __/ _ \ / _` |/ _ \
        | |_) | (_) | | | (__| |_| | | (_| \__ \ | (_| (_) | (_| |  __/
        | .__/ \___/|_|_|\___|\__, |  \__,_|___/  \___\___/ \__,_|\___|
        |_|                   |___/

```
___
This repo and it's content were made to reflect the ideas in [this blog post](https://www.adamgroenhout.com/organizational-security-policy-as-code/)
___

# Policy as Code

This repository contains our organization's policies, managed as code. This approach allows us to maintain our policies with the same rigor and transparency as our software, ensuring they are always up-to-date, auditable, and aligned with our operational realities.

## The Policy as Code Philosophy

Managing policies as code transforms them from static documents into a dynamic and integrated part of our governance framework. By leveraging version control, automation, and collaborative tools like Git, we address common challenges such as outdated policies, unstructured feedback, and a lack of transparency.

This framework is built on the following principles:
- **Version Control and Auditability:** Every change is tracked in Git, creating a complete audit trail of who changed what, when, and why.
- **Automated Workflows:** Policy updates are automatically published, and stakeholders are notified of changes, eliminating manual and error-prone processes.
- **Structured Metadata:** Policies are enriched with metadata, enabling automation and better integration with our compliance and risk management processes.
- **Collaboration and Transparency:** The entire policy lifecycle is managed in the open, fostering a culture of shared responsibility for security and compliance.

## Policy Architecture

Our policy framework consists of four types of documents, each with a distinct purpose:

- **Policies:** High-level statements of *what* is required. Policies are broad and do not go into implementation details. They articulate the organization's stance on a particular issue (e.g., "All access to sensitive data must be logged").
- **Standards:** Define *how* the high-level policy requirements are met. Standards provide specific, mandatory controls and technologies (e.g., "All database access must be logged to the central SIEM using the approved logging agent").
- **Processes:** The step-by-step implementation of standards. Processes are detailed, operational documents that guide teams in their day-to-day activities (e.g., "How to configure database logging for a new application").
- **Guidance:** Non-mandatory, recommended best practices. Guidance provides helpful advice and examples to assist with the implementation of standards and processes (e.g., "Examples of effective database log queries for threat hunting").

## Repository Structure

This repository is organized as follows:

- **/policies:** This directory contains all our high-level policy documents in Markdown format. These documents define *what* is required.
- **/standards:** This directory contains our standards documents, which define *how* our high-level policy requirements are met with specific, mandatory controls.
- **/processes:** This directory contains our process documents, which provide step-by-step instructions for implementing specific standards.
- **/guidance:** This directory contains our guidance documents, which provide non-mandatory, recommended best practices.
- **.github/CODEOWNERS:** This file automatically assigns reviewers for pull requests based on the policy being changed.
- **.github/workflows/publish-policies.yml:** This GitHub Actions workflow automates the publishing of all documents to GitHub Pages whenever a change is merged into the `main` branch.
- **/templates:** This directory contains templates for each document type to enforce a consistent structure.

## Automated Validation

To ensure consistency and adherence to our defined structure, this repository uses an automated validation system. Each document type has a corresponding template located in the `/templates` directory. These templates define the required frontmatter (metadata) and section headings for each document.

When a pull request is opened that modifies any markdown files, a GitHub Actions workflow automatically runs a validation script (`validate.py`). This script checks the changed documents against their respective templates to ensure they are compliant. This validation must pass before a pull request can be merged.

### Local Validation
You can run the validation linter locally to check all documents in the repository. This is useful for verifying your changes before opening a pull request.

1.  **Install Dependencies:**
    ```bash
    pip install poetry
    poetry install
    ```

2.  **Run the Linter:**
    ```bash
    poetry run python linter.py
    ```

## Change Management Process

All changes to policies must be made through a pull request. This process ensures that all changes are reviewed and approved before being integrated into the official policies.

To propose a change:
1.  **Create a Branch:** Create a new branch from `main` with a descriptive name (e.g., `feature/update-access-control-policy` or `fix/typo-in-data-security-policy`).
2.  **Make Your Changes:** Edit the relevant policy file(s) in your branch.
3.  **Open a Pull Request:** Open a pull request from your branch to `main`. The pull request description should include:
    - A clear explanation of the proposed change.
    - The rationale for the change (the "why").
    - A link to any relevant tickets or project documentation.
4.  **Request Reviews:** The `CODEOWNERS` file will automatically assign the appropriate reviewers. You should also notify any other relevant stakeholders.
5.  **Merge:** Once the pull request has been approved by the required reviewers, it can be merged into `main`.

## Branch Protection Rules

The `main` branch is protected by the following rules to ensure the integrity of our policies:

- **Require a pull request before merging:** All changes must be made through a pull request. Direct pushes to `main` are blocked.
- **Require approvals:** Pull requests must be approved by at least one of the designated code owners before they can be merged.
- **Dismiss stale pull request approvals when new commits are pushed:** If a pull request is updated with new changes, any previous approvals are dismissed, and the changes must be reviewed again.
- **Require status checks to pass before merging:** Any automated checks (e.g., linting, validation) must pass before a pull request can be merged. (Note: No status checks are configured in this initial setup, but this rule is recommended for future enhancements).
