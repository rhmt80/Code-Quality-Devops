# Code-Quality-Devops
Python Code Quality and CI/CD Pipeline

# Python Code Quality and CI/CD Pipeline

## Overview

This project is a **Python Code Quality Pipeline** that automatically performs static code analysis, security scanning, and testing, integrated with **GitHub Actions** and **SonarCloud**.  
The pipeline ensures that Python code is **maintainable, secure, and compatible across multiple Python versions** (3.9, 3.10, 3.11).

It is designed to enforce coding standards, catch bugs early, and provide continuous feedback through **SonarCloud dashboards**.

---

## Features

- **Static Code Analysis**
  - `flake8` for PEP8 compliance and style issues
  - `pylint` for detecting errors, code smells, and enforcing coding standards
  - `black` (optional) for automatic code formatting

- **Security Scan**
  - `bandit` scans Python code for common security vulnerabilities

- **Unit Testing**
  - `pytest` runs tests across multiple Python versions
  - Test results are stored in `junit` folder and can be uploaded as artifacts

- **CI/CD Integration**
  - Fully automated GitHub Actions workflow
  - Multi-version Python testing (3.9, 3.10, 3.11)
  - SonarCloud integration for code quality metrics

- **Code Quality Dashboard**
  - SonarCloud provides detailed insights:
    - Bugs, vulnerabilities, and code smells
    - Test coverage (if integrated)
    - Code duplication and complexity

## Project Structure

---code_quality2/
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

- **GitHub Actions Workflow**

- Runs automatically on push or pull request to the main branch.
- Steps include:
 - Checkout code
 - Setup Python (3.9, 3.10, 3.11)
 - Install dependencies
 - Lint with Flake8 & Pylint
 - Optional Black formatting check
 - Security scan with Bandit
 - Run tests with Pytest
 - Upload results and analyze with SonarCloud


