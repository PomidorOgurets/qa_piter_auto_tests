import pytest
from playwright.sync_api import Playwright, sync_playwright

# Фикстура для открытия чистой страницы в браузере Хром

@pytest.fixture(scope="function")
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
