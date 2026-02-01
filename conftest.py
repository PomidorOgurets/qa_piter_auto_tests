import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture(scope="function", autouse=True)
def browser_setting():
    browser = sync_playwright().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://piter-online.net/")

    yield

    context.close()
    browser.close()