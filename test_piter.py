import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://piter-online.net/")
    page.get_by_role("combobox", name="Введите улицу").click()
    page.get_by_role("combobox", name="Введите улицу").fill("Тестовая линия")
    page.get_by_text("Тестовая линия").click()
    page.get_by_role("combobox", name="Дом").fill("1")
    page.get_by_role("combobox", name="Дом").press("Enter")
    time.sleep(2)
    page.get_by_role("button", name="Найти тарифы").click()
    page.get_by_role("textbox", name="+7 (").click()
    page.get_by_role("textbox", name="+7 (").fill("+7 (111) 111-11-111")
    page.get_by_role("button", name="Показать результаты").click()
    time.sleep(5)
    page.get_by_role("button", name="Смотреть тарифы").click()
    expect(page.get_by_role("heading", name="Интернет и ТВ по адресу Ленинградская область, линия Тестовая")).to_be_visible()
    time.sleep(10)
    response = page.goto("https://piter-online.net/")

    assert response.status == 200, f"Главная страница вернула статус {response.status} вместо 200"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
