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
    PiterOnline.expect_tariffs_heading_visible()


@pytest.mark.parametrize("run", range(1))
def test_change_region(page, run):
    PiterOnline = MainPage(page)
    PiterOnline.open_main_site()
    PiterOnline.open_region_menu()
    PiterOnline.select_gatchina_region()
    PiterOnline.expect_gatchina_visible()


@pytest.mark.parametrize("run", range(5))
def test_status(page, run):
    # Переход на главную и проверка HTTP 200
    response = page.goto(BASE_URL)
    assert response.status == 200, f"Главная страница вернула статус {response.status} вместо 200"








