import pytest
from playwright.sync_api import expect
from Data.constants import *
from Data.test_data import *
from pages.main_page import MainPage

@pytest.mark.parametrize("run", range(5))
def test_fill_page(page, run):
    PiterOnline = MainPage(page)
    PiterOnline.open_main_site()
    PiterOnline.fill_complete_form(TEST_STREETS[0], TEST_HOUSES[0], TEST_PHONES[0])

    expect(page.get_by_role("heading", name=HEADING_TARIFFS_PATTERN)).to_be_visible()


@pytest.mark.parametrize("run", range(5))
def test_change_region(page, run):
    page.goto("https://piter-online.net/")
    page.get_by_role("banner").get_by_role("link", name=REGION_DEFAULT).click()
    page.get_by_role("link", name=REGION_GATCHINA).click()
    expect(page.get_by_text(REGION_GATCHINA_TEXT, exact=True)).to_be_visible()


@pytest.mark.parametrize("run", range(5))
def test_status(page, run):
    # Переход на главную и проверка HTTP 200
    response = page.goto(BASE_URL)
    assert response.status == 200, f"Главная страница вернула статус {response.status} вместо 200"








