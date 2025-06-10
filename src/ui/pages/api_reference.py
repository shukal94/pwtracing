from playwright.sync_api import Locator, Page
from src.ui.pages.base import BasePage


class ApiReferencePage(BasePage):
    heading_label: Locator

    def __init__(self, page: Page):
        super().__init__(page, "/docs/intro")
        self.heading_label = self.page.get_by_role("heading", name="Installation")
