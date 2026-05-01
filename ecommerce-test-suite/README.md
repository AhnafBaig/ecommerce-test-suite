# E-Commerce Test Automation Suite

A BDD test automation framework covering **UI** and **REST API** layers using Playwright, pytest-bdd, and Gherkin.

![Test Status](https://github.com/YOUR_USERNAME/ecommerce-test-suite/actions/workflows/tests.yml/badge.svg)

---

## Structure

```
ecommerce-test-suite/
├── features/               # Gherkin BDD feature files
│   ├── login.feature
│   ├── shopping_cart.feature
│   └── api/rest_api.feature
├── pages/                  # Page Object Model (POM) classes
├── steps/                  # BDD step definitions (ui/ and api/)
├── tests/                  # pytest entry points
├── utils/config.py         # Centralised config + env vars
├── .github/workflows/      # GitHub Actions CI/CD
└── conftest.py             # Shared fixtures
```

---

## Tech Stack

| Layer       | Tool                 |
|-------------|----------------------|
| Language    | Python 3.12          |
| UI Testing  | Playwright           |
| BDD         | pytest-bdd + Gherkin |
| API Testing | Requests             |
| Reports     | pytest-html          |
| CI/CD       | GitHub Actions       |

---

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-test-suite.git
cd ecommerce-test-suite

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install chromium
```

---

## Running Tests

```bash
pytest                           # All tests
pytest tests/ui/ -v              # UI only
pytest tests/api/ -v             # API only
HEADLESS=false pytest tests/ui/  # Headed browser (great for demos)
```

Reports are saved to `reports/report.html` after every run.

---

## CI/CD

| Trigger             | What runs                  |
|---------------------|----------------------------|
| Push / PR           | Smoke suite (API)          |
| Schedule (2 AM UTC) | Full regression (UI + API) |
| Manual dispatch     | Choose: all, ui, or api    |

Add secrets under **Repo → Settings → Secrets → Actions**: `STANDARD_USER`, `PASSWORD`

---

## Targets

| Layer | App |
|-------|-----|
| UI    | [SauceDemo](https://www.saucedemo.com) |
| API   | [JSONPlaceholder](https://jsonplaceholder.typicode.com) |
