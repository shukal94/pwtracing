import pytest
from playwright.sync_api import expect
from src.ui.pages.api_reference import ApiReferencePage
from src.ui.pages.start import StartPage


@pytest.mark.smoke
def test_get_started_link(page):
    start_page = StartPage(page)
    start_page.open()
    start_page.get_started_link.click()
    api_reference_page = ApiReferencePage(page)
    expect(api_reference_page.heading_label).to_be_visible()
