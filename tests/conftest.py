import json

import pytest
import src.utils as utils
from playwright.sync_api import sync_playwright


CONFIG_PATH = "config.ini"


@pytest.fixture(scope="session")
def config():
    return utils.load_config(path=CONFIG_PATH)


@pytest.fixture(scope="function")
def pw():
    with sync_playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture(scope="function")
def browser(config, pw):
    ui_config = config["ui"]
    browser_name = ui_config.get("browser_name")
    headless = ui_config.getboolean("headless")
    timeout = ui_config.getint("timeout")

    if browser_name == "chromium":
        browser = pw.chromium.launch(headless=headless, timeout=timeout)
    elif browser_name == "firefox":
        browser = pw.firefox.launch(headless=headless, timeout=timeout)
    elif browser_name == "webkit":
        browser = pw.webkit.launch(headless=headless, timeout=timeout)
    else:
        raise RuntimeError(f"Unknown browser: {browser_name}")

    yield browser

    browser.close()


@pytest.fixture(scope="function")
def browser_context(config, browser):
    ui_config = config["ui"]
    base_url = ui_config.get("base_url")
    viewport = json.loads(ui_config.get("viewport"))
    ctx = browser.new_context(viewport=viewport, base_url=base_url)

    yield ctx

    ctx.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()

    yield page

    page.close()