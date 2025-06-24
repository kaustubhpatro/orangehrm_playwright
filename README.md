# OrangeHRM Playwright Test Framework

A Playwright + pytest automation framework to verify login and sidebar navigation (Admin, PIM, Leave) on the OrangeHRM demo site.

---

## Repository URL

```bash
git clone https://github.com/kaustubhpatro/orangehrm_playwright.git
cd orangehrm_playwright
```

---

## Project Structure

```
orangehrm_playwright/
├── config/
│   └── creds.json          # JSON file with login credentials
├── pages/
│   ├── login_page.py        # Page Object: login actions & locators
│   └── dashboard_page.py    # Page Object: navigation & header checks
├── tests/
│   ├── conftest.py          # pytest fixtures: load creds, auth state, provide page/objects
│   └── test_navigation.py   # Parametrized test for Admin/PIM/Leave links
├── pytest.ini               # pytest-playwright config (browsers, headed)
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## Credentials File (`config/creds.json`)

Store your OrangeHRM username and password here:

```json
{
  "username": "Admin",
  "password": "admin123"
}
```
---

##  Requirements & Setup

1. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate       # macOS/Linux
   .venv\\Scripts\\activate      # Windows
   ```

2. **Install dependencies**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   playwright install                # download browsers
   ```

---

## Configuration (`pytest.ini`)

```ini
[pytest]
addopts = --browser chromium --browser firefox --browser webkit --headed --alluredir=reports/allure-results
```

* **--browser** flags run tests on Chromium, Firefox, and WebKit.
* **--headed** launches browsers with UI (headless=False).

---

## Fixtures (`tests/conftest.py`)

| Fixture Name     | Scope    | Purpose                                                                                     |
| ---------------- | -------- |---------------------------------------------------------------------------------------------|
| `credentials`    | session  | Load JSON credentials from `config/creds.json`.                                                |
| `storage_state`  | session  | Launch browser, perform login once per engine, save storageState to temp file.              |
| `page_with_auth` | function | Create new context using saved storageState, navigate to login URL, ensure session applies. |
| `dashboard`      | function | Provide a `DashboardPage` instance for tests.                                               |

**Flow**: login → save cookies/localStorage → reuse for each test page.

---

## Page Objects

### `pages/login_page.py`

* **Purpose**: Encapsulate login steps using XPath.

### `pages/dashboard_page.py`

* **Purpose**: Encapsulate sidebar navigation and header retrieval using XPath.
---

## Test File

### `tests/test_navigation.py`

Parametrized test mapping sidebar labels to expected page titles:

---

## Running Tests Locally

From project root:

```bash
pytest
```

You will see tests run in **Chromium**, **Firefox**, and **WebKit** in headed mode.

---

## Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/X`)
3. Add the changed file (`git add file_name.py`)
4. Make changes and commit (`git commit -m "added new code"`)
5. Push branch and open a Pull Request

---
