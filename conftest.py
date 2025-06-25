import json
import logging
import pytest
from pathlib import Path
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# load credentials
CONFIG_PATH = Path(__file__).resolve().parent.parent / "orangehrm_playwright" / "config" / "creds.json"


@pytest.fixture(scope="session")
def credentials():
    creds = json.loads(CONFIG_PATH.read_text())
    logger.info("Loaded credentials from config")
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
    logger.info(f"Saved storage state for {browser_name}")
    return state_file


@pytest.fixture
def page_with_auth(browser, storage_state):
    context = browser.new_context(storage_state=str(storage_state))
    pages = context.pages
    page = pages[0] if pages else context.new_page()
    page.goto(LoginPage.URL)
    page.wait_for_selector("aside nav")
    return page


@pytest.fixture
def dashboard(page_with_auth):
    return DashboardPage(page_with_auth)


# screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page_with_auth")
        if page:
            path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=path)
            logger.error(f"Screenshot captured: {path}")
