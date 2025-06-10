from playwright.sync_api import Page


class BasePage:
    page: Page
    url: str

    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(url=self.url)
