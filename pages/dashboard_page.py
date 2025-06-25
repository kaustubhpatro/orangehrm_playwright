from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def click_panel(self, panel: str):
        self.page.get_by_role("link", name=panel).click()
        self.page.wait_for_selector("h6.oxd-text--h6")

    def get_header(self) -> str:
        return (
            self.page
                .locator("h6.oxd-text--h6:last-of-type")
                .inner_text()
                .strip()
        )
