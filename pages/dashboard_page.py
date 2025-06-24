from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def click_panel(self, panel: str):
        self.page.locator(f"xpath=//span[text()='{panel}']").click()
        self.page.wait_for_selector("xpath=//h6[contains(@class,'oxd-text--h6')]")

    def get_header(self) -> str:
        return (
            self.page
            .locator("xpath=(//h6[contains(@class,'oxd-text--h6')])[last()]")
            .inner_text()
            .strip()
        )
