# Code-Quality-DevOps

![Python](https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11-blue)
![GitHub Actions](https://img.shields.io/badge/CI-CD-GitHub%20Actions-orange)
![SonarCloud](https://img.shields.io/badge/Code%20Quality-SonarCloud-brightgreen)

---

## Overview

**Code-Quality-DevOps** is a **Python Code Quality and CI/CD Pipeline** project that automates:

- Static code analysis  
- Security scanning  
- Unit testing  

It is integrated with **GitHub Actions** and **SonarCloud**, ensuring your Python code is:

- Maintainable  
- Secure  
- Compatible across multiple Python versions (3.9, 3.10, 3.11)  

The pipeline enforces coding standards, catches bugs early, and provides continuous feedback through **SonarCloud dashboards**.

---

## Features

### 1. Static Code Analysis
- **Flake8:** Checks PEP8 compliance and style issues  
- **Pylint:** Detects errors, code smells, and enforces coding standards  
- **Black (optional):** Automatically formats code according to style rules  

### 2. Security Scan
- **Bandit:** Scans Python code for common security vulnerabilities  

### 3. Unit Testing
- **Pytest:** Runs tests across multiple Python versions  
- Stores results in the `junit/` folder, which can be uploaded as artifacts in CI  

### 4. CI/CD Integration
- Fully automated **GitHub Actions workflow**  
- Multi-version Python testing (3.9, 3.10, 3.11)  
- SonarCloud integration for code quality metrics  

### 5. Code Quality Dashboard
- SonarCloud provides detailed insights including:
  - Bugs, vulnerabilities, and code smells  
  - Test coverage (if integrated)  
  - Code duplication and complexity  

---

## Project Structure

- code_quality2/
├─ my_module/
│ └─ calculator.py # Main Python module with functions
├─ tests/
│ └─ test_calculator.py # Unit tests
├─ junit/ # Test results folder (created by GitHub Actions)
├─ .github/workflows/ci.yml # GitHub Actions workflow for CI/CD
├─ .sonarcloud.properties # SonarCloud configuration
├─ pyproject.toml # Pylint and Black configuration
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation

---

## GitHub Actions Workflow

The CI/CD pipeline runs automatically on **push** or **pull request** to the `main` branch.  
**Workflow steps include:**

1. Checkout code  
2. Setup Python environments (3.9, 3.10, 3.11)  
3. Install dependencies from `requirements.txt`  
4. Lint code using **Flake8** and **Pylint**  
5. Optional code formatting check using **Black**  
6. Security scan with **Bandit**  
7. Run unit tests with **Pytest**  
8. Upload results and analyze code quality with **SonarCloud**

