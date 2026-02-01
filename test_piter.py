import time
from playwright.sync_api import expect

def test_fill_page(page):

    page.goto("https://piter-online.net/")
    page.get_by_role("combobox", name="Введите улицу").click()
    page.get_by_role("combobox", name="Введите улицу").fill("Тестовая линия")
    page.get_by_text("Тестовая линия").click()
    page.get_by_role("combobox", name="Дом").fill("1")
    page.get_by_role("combobox", name="Дом").press("Enter")

    time.sleep(1) # Надо поменять на что-то
    page.get_by_role("button", name="Найти тарифы").wait_for(state="visible", timeout=10000)
    page.get_by_role("button", name="Найти тарифы").click()

    page.get_by_role("textbox", name="+7 (").fill("+7 (111) 111-11-111")
    page.get_by_role("button", name="Показать результаты").click()


    page.get_by_role("button", name="Смотреть тарифы").wait_for(state="visible", timeout=10000)
    page.get_by_role("button", name="Смотреть тарифы").click()


    expect(page.get_by_role("heading", name="Интернет и ТВ по адресу Ленинградская область, линия Тестовая")).to_be_visible()


def test_change_region(page):
    page.goto("https://piter-online.net/")
    page.get_by_role("banner").get_by_role("link", name="Санкт-Петербург").click()
    page.get_by_role("link", name="Гатчина Ленинградская область").click()
    expect(page.get_by_text("Гатчина", exact=True)).to_be_visible()

def test_status(page):
    # Переход на главную и проверка HTTP 200
    response = page.goto("https://piter-online.net/")
    assert response.status == 200, f"Главная страница вернула статус {response.status} вместо 200"








