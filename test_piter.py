import pytest
from Data.constants import *
from Data.test_data import *
from pages.main_page import MainPage


# Автоматизация подачи заявки
@pytest.mark.parametrize("run", range(5))
def test_fill_page(page, run):
    PiterOnline = MainPage(page)
    PiterOnline.open_main_site()
    PiterOnline.fill_complete_form(TEST_STREETS[0], TEST_HOUSES[0], TEST_PHONES[0])
    PiterOnline.expect_tariffs_heading_visible()


# Смена региона и проверка изменения страницы
@pytest.mark.parametrize("run", range(5))
def test_change_region(page, run):
    PiterOnline = MainPage(page)
    PiterOnline.open_main_site()
    PiterOnline.open_region_menu()
    PiterOnline.select_gatchina_region()
    PiterOnline.expect_gatchina_visible()


# Переход на главную и проверка статуса HTTP 200
@pytest.mark.parametrize("run", range(5))
def test_status(page, run):
    response = page.goto(BASE_URL)
    assert response.status == 200, f"Главная страница вернула статус {response.status} вместо 200"








