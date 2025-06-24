import json
import pytest
from pathlib import Path
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

CONFIG_PATH = Path(__file__).resolve().parent.parent / "orangehrm_playwright" / "config" / "creds.json"


@pytest.fixture(scope="session")
def credentials():
    with open(CONFIG_PATH) as f:
        creds = json.load(f)
    assert "username" in creds and "password" in creds
    return creds


@pytest.fixture(scope="session")
def storage_state(tmp_path_factory, credentials, browser, request):
    browser_name = request.config.getoption("--browser")
    state_file = tmp_path_factory.mktemp("state") / f"{browser_name}-state.json"
    context = browser.new_context()
    page = context.new_page()
    login = LoginPage(page)
    login.goto()
    login.login(credentials["username"], credentials["password"])
    context.storage_state(path=state_file)
    context.close()

    return state_file


@pytest.fixture
def page_with_auth(browser, storage_state):
    context = browser.new_context(storage_state=str(storage_state))
    pages = context.pages
    page = pages[0] if pages else context.new_page()
    page.goto(LoginPage.URL)
    page.wait_for_selector("xpath=//aside")
    yield page
    context.close()


@pytest.fixture
def dashboard(page_with_auth):
    return DashboardPage(page_with_auth)
