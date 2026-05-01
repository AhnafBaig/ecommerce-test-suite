# 🧪 E-Commerce Test Automation Suite

A production-quality BDD test automation framework covering **UI** and **REST API** layers,
built to demonstrate QA engineering skills for roles requiring Playwright, Selenium, Cucumber,
CI/CD pipelines, and test management practices.

![Test Status](https://github.com/YOUR_USERNAME/ecommerce-test-suite/actions/workflows/tests.yml/badge.svg)

---

## 🏗️ Architecture Overview

```
ecommerce-test-suite/
│
├── features/                   # Gherkin BDD feature files
│   ├── login.feature           # User authentication scenarios
│   ├── shopping_cart.feature   # Cart management scenarios
│   └── api/
│       └── rest_api.feature    # REST API contract scenarios
│
├── pages/                      # Page Object Model (POM) classes
│   ├── base_page.py            # Shared base class for all pages
│   ├── login_page.py           # Login page interactions
│   ├── inventory_page.py       # Product listing interactions
│   └── cart_page.py            # Cart page interactions
│
├── steps/                      # BDD step definitions
│   ├── ui/
│   │   ├── login_steps.py      # Given/When/Then for login
│   │   └── cart_steps.py       # Given/When/Then for cart
│   └── api/
│       └── api_steps.py        # Given/When/Then for REST API
│
├── tests/                      # pytest entry points (bind scenarios)
│   ├── ui/
│   │   ├── test_login.py
│   │   └── test_shopping_cart.py
│   └── api/
│       └── test_rest_api.py
│
├── utils/
│   └── config.py               # Centralised config + env vars
│
├── .github/workflows/
│   └── tests.yml               # CI/CD pipeline (GitHub Actions)
│
├── conftest.py                 # Shared fixtures + step registration
├── pytest.ini                  # pytest config
├── requirements.txt            # Python dependencies
└── .env                        # Local env vars (not committed)
```

---

## ⚙️ Tech Stack

| Layer       | Tool / Library         | Purpose                              |
|-------------|------------------------|--------------------------------------|
| Language    | Python 3.12            | Primary automation language          |
| UI Testing  | Playwright             | Fast, reliable cross-browser UI      |
| BDD         | pytest-bdd + Gherkin   | Human-readable test scenarios        |
| API Testing | Requests               | HTTP client for REST API assertions  |
| Runner      | pytest                 | Test orchestration and reporting     |
| Reports     | pytest-html            | HTML test execution reports          |
| CI/CD       | GitHub Actions         | Smoke on push, regression nightly    |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-test-suite.git
cd ecommerce-test-suite
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure environment variables
Copy `.env` and adjust if needed (defaults work out of the box):
```bash
cp .env .env.local
```

---

## ▶️ Running Tests

### Run all tests
```bash
pytest
```

### Run only UI tests
```bash
pytest tests/ui/ -v
```

### Run only API tests
```bash
pytest tests/api/ -v
```

### Run tests with visible browser (headed mode)
```bash
HEADLESS=false pytest tests/ui/ -v
```

### Run with slow motion (great for demos)
```bash
HEADLESS=false SLOW_MO=500 pytest tests/ui/ -v
```

---

## 📊 Test Reports

After any test run, an HTML report is generated at:
```
reports/report.html
```
Open it in any browser. It includes pass/fail status, duration, and full stack traces on failures.

---

## 🔁 CI/CD Pipeline

The GitHub Actions pipeline (`.github/workflows/tests.yml`) runs automatically:

| Trigger              | What runs                        |
|----------------------|----------------------------------|
| Push / Pull Request  | Smoke suite (API tests only)     |
| Schedule (2 AM UTC)  | Full regression (UI + API)       |
| Manual dispatch      | Choose: `all`, `ui`, or `api`    |

Test reports are uploaded as **build artifacts** — downloadable from the Actions run summary.

To add secrets for CI (credentials), go to:
`GitHub repo → Settings → Secrets and variables → Actions`

Add:
- `STANDARD_USER`
- `PASSWORD`

---

## 🧩 Design Patterns

### Page Object Model (POM)
All UI interactions are encapsulated in `pages/`. Tests never reference selectors directly — this means a single selector change only needs to be updated in one place.

### BDD (Behaviour-Driven Development)
Feature files in `features/` are written in plain English (Gherkin). This makes test intent readable by non-technical stakeholders. Step definitions in `steps/` wire the English to Python.

### Separation of Concerns
```
Feature file (WHAT to test)  →  Step definitions (HOW in plain Python)  →  Page Objects (WHERE the element is)
```

---

## 🐛 Defect Tracking

Bugs found during test runs are tracked as **GitHub Issues** with the following labels:
- `bug` — confirmed defect
- `ui` / `api` — affected layer
- `priority: high/medium/low` — severity

Each issue links back to the failing test scenario for full traceability.

---

## 📚 Targets Under Test

| Layer | Application                                     |
|-------|-------------------------------------------------|
| UI    | [SauceDemo](https://www.saucedemo.com)          |
| API   | [JSONPlaceholder](https://jsonplaceholder.typicode.com) |
