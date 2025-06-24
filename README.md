**Heroku API Testing Framework**

A Python `pytest`-based test suite for the [Heroku booking](https://restful-booker.herokuapp.com) API. Implements tests for authentication, booking creation, partial updates, and retrieval, with Allure reporting, randomized payloads via Faker, and clean fixture-driven architecture.

---

## 📖 Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation & Setup](#installation--setup)
4. [Project Structure](#project-structure)
5. [API Client](#api-client)
6. [Fixtures](#fixtures)
7. [Test Cases](#test-cases)
8. [Running Tests](#running-tests)
9. [Allure Reporting](#allure-reporting)
10. [Contributing](#contributing)

---

## Project Overview

This framework provides:

* **API client abstraction** (`utils/api_client.py`) for all HTTP operations
* **Pytest fixtures** for reusable setup: session client, auth token, randomized booking payload
* **Test modules** covering:

  * Authentication (`tests/test_auth.py`)
  * Create Booking (`tests/test_create.py`)
  * Partial Update (`tests/test_partial_update.py`)
  * Get Booking (`tests/test_get_booking.py`)
* **Allure reporting** for detailed, interactive test reports
* **Parameterization-ready** structure for future expansion

---

## Prerequisites

* Python 3.8+
* Git
* (Optional) [Allure CLI](https://docs.qameta.io/allure/)

---

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/kaustubhpatro/heroku_api_test.git
   cd heroku_booking_tests
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Project Structure

```text
restful-booker-tests/
├── reports/                   # Allure report results & HTML
├── tests/
│   ├── test_auth.py           # Auth endpoint tests
│   ├── test_create.py         # Create booking tests
│   ├── test_partial_update.py # Partial update tests
│   ├── test_get_booking.py    # Get booking tests
│   └── test_cleanup.py        # (Optional) cleanup / delete tests
├── utils/
│   └── api_client.py          # HTTP client for Restful Booker API
├── conftest.py                # Pytest fixtures
├── requirements.txt           # Project dependencies
├── pytest.ini                 # Pytest configuration & logging
└── README.md                  
```

---

## API Client

Located in `utils/api_client.py`, the `APIClient` class:

* Manages the base URL
* Implements methods for:

  * `auth(username, password) -> token`
  * `create(payload) -> {bookingid, booking}`
  * `partial_update(id, payload, token) -> updated_fields`
  * `get(id) -> booking_details`

All methods:

* Use `requests` under the hood
* Call `raise_for_status()` for HTTP errors
* Return parsed JSON or status for assertions

---

## Fixtures

Defined in `tests/conftest.py`, available to all tests:

| Fixture Name      | Scope    | Returns                                | Usage                                    |
| ----------------- | -------- | -------------------------------------- | ---------------------------------------- |
| `client`          | session  | `APIClient` instance                   | Call any API endpoint                    |
| `token`           | session  | Authentication token string            | Required for `partial_update`|
| `booking_payload` | function | Randomized `dict` for create/patch/get | Clean, reusable test data                |

* **`booking_payload`** uses `Faker` for names, Python `random` for price/boolean, and dates based on `date.today()`.

---

## Test Cases

| File                     | Endpoint Tested        | Description                     |
| ------------------------ | ---------------------- | ------------------------------- |
| `test_auth.py`           | `POST /auth`           | Valid & invalid credentials     |
| `test_create.py`         | `POST /booking`        | Create booking, assert all data |
| `test_partial_update.py` | `PATCH /booking/{id}`  | Partial update (lastname)       |
| `test_get_booking.py`    | `GET /booking/{id}`    | Retrieve & verify full booking  |
* Tests use **assertions** on both status and payload content.

## Running Tests

1. **Run full suite**:

   ```bash
   pytest
   ```

2. **Run in parallel** (requires `pytest-xdist`):

   ```bash
   pytest -n auto
   ```

3. **Run a single test file**:

   ```bash
   pytest tests/test_create.py
   ```

4. **View detailed logs**: enabled by `log_cli = true` in `pytest.ini`.

---

## Allure Reporting

1. **Collect results** (configured in `pytest.ini`):

   ```bash
   pytest --alluredir=reports/allure-results
   ```

2. **Serve interactive report**:

   ```bash
   allure serve reports/allure-results
   ```

3. **Generate static HTML**:

   ```bash
   allure generate reports/allure-results -o reports/allure-report --clean
   ```

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/somethingnew`)
3. Add the changed file(`git add file_name.py`)
4. Make changes & commit (`git commit -m 'Added some new code'`)
5. Push to branch (`git push origin feature/somethingnew`)
6. Open a Pull Request

---