from playwright.sync_api import Locator, Page
from src.ui.pages.base import BasePage


class StartPage(BasePage):
    get_started_link: Locator

    def __init__(self, page: Page):
        super().__init__(page, "/")
        self.get_started_link = page.get_by_role("link", name="Get started")
