
---

# Selenium Tests Resolver

A test automation project built using **Selenium** and **Pytest**, designed to execute automated UI tests and generate detailed test reports with **Allure**. This repository demonstrates best practices for test automation and GitHub Actions CI/CD workflows.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Test Reports](#test-reports)
- [Links](#links)
- [How to Run Locally](#how-to-run-locally)
- [Folder Structure](#folder-structure)

---

## Project Overview

The **Selenium Tests Resolver** project automates the testing of web applications using Selenium WebDriver and generates visual test reports using Allure. It integrates seamlessly with GitHub Actions for continuous testing and deployment.

The test results and associated documentation are hosted on GitHub Pages.

---

## Technologies Used

- **Programming Language**: Python (3.11)
- **Test Framework**: Pytest
- **Reporting**: Allure
- **Browser**: Google Chrome (via ChromeDriver)
- **Continuous Integration**: GitHub Actions
- **Hosting**: GitHub Pages

---

## Features

- Automated testing of web applications using Selenium using POM.
- Detailed test reports generated with Allure.
- Continuous integration and deployment via GitHub Actions.
- Hosted test reports and guides for easy sharing.

---

## Test Reports

### Allure Report

The latest Allure report can be accessed here:

- [Allure Report](https://dinabutko.github.io/selenium-tests-resolver/reports)

The Allure report provides:
- Test execution results.
- Logs and screenshots for failed tests.
- Graphical analysis of test results.

---

## Links

- **Home Page**: [Selenium Tests Resolver Home](https://dinabutko.github.io/selenium-tests-resolver/)
- **QE Guide**: [QE Guide](https://dinabutko.github.io/selenium-tests-resolver/QE-guide/)
- **Allure Report**: [Allure Report](https://DinaButko.github.io/selenium-tests-resolver/reports)

---

## How to Run Locally

### Prerequisites
- Python 3.11 or higher
- Google Chrome installed
- ChromeDriver compatible with your Chrome version
- Dependencies from `requirements.txt`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/dinabutko/selenium-tests-resolver.git
   cd selenium-tests-resolver
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   pytest --alluredir=allure-results
   ```

4. Generate the Allure report:
   ```bash
   allure generate allure-results --clean -o report
   ```

5. Serve the Allure report locally:
   ```bash
   cd report
   python -m http.server 8080
   ```
   Open `http://localhost:8080` in your browser to view the report.

---

## Folder Structure

```
selenium-tests-resolver/
├── .github/workflows/         # GitHub Actions workflow for CI/CD
├── allure-results/            # Allure raw results (generated after running tests)
├── QE-guide/                  # QE Guide resources
├── report/                    # Allure report (HTML content)
├── pages/                     # Selenium page object files
│   ├── base_page.py           # Base class for all pages
│   ├── home_page.py           # Home page-specific elements and actions
│   └── guide_page.py          # QE Guide page-specific elements and actions
├── tests/                     # Test files
│   ├── test_home.py           # Tests for the home page
│   ├── conftest.py            # Pytest fixtures and configurations
├── utilities/                 # Helper functions (e.g., logging)
├── README.md                  # Project overview (this file)
├── requirements.txt           # Python dependencies
└── index.html                 # Home page for GitHub Pages
```

---

## CI/CD Workflow

The project uses GitHub Actions for continuous testing and deployment:

1. **Run Tests**:
   - Pytest runs the automated tests and saves results in the `allure-results` directory.
2. **Generate Report**:
   - Allure CLI generates the test report in the `report` directory.
3. **Deploy**:
   - GitHub Pages hosts the custom home page, QE Guide, and Allure report.

---
