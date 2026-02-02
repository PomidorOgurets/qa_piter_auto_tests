import pytest
import allure
from allure_commons.types import AttachmentType
from Data.constants import *
from Data.test_data import *
from pages.main_page import MainPage


# Автоматизация подачи заявки
@pytest.mark.parametrize("run", range(5))
@allure.title("Подача заявки")
@allure.description("Заполнение формы адрес+телефон, переход к тарифам")
def test_fill_page(page, run):
    with allure.step(f"Открытие главной страницы - {BASE_URL}"):
        PiterOnline = MainPage(page)
        PiterOnline.open_main_site()

    with allure.step(f"Заполнение формы: {TEST_STREETS[0]}, дом {TEST_HOUSES[0]}, тел {TEST_PHONES[0]}"):
        PiterOnline.fill_complete_form(TEST_STREETS[0], TEST_HOUSES[0], TEST_PHONES[0])

    with allure.step("Проверка заголовка тарифов"):
        PiterOnline.expect_tariffs_heading_visible()

    allure.attach(page.screenshot(), name="Final screenshot", attachment_type=AttachmentType.PNG)


# Смена региона и проверка изменения страницы
@pytest.mark.parametrize("run", range(5))
@allure.title("Смена региона на Гатчину")
@allure.description("Открытие меню регионов → выбор Гатчины → проверка текста")
def test_change_region(page, run):
    with allure.step(f"Открытие главной страницы - {BASE_URL}"):
        PiterOnline = MainPage(page)
        PiterOnline.open_main_site()

    with allure.step("Открытие меню выбора региона"):
        PiterOnline.open_region_menu()

    with allure.step("Выбор Гатчины как региона"):
        PiterOnline.select_gatchina_region()

    with allure.step("Проверка, что регион поменялся на Гатчину"):
        PiterOnline.expect_gatchina_visible()


# Переход на главную и проверка статуса HTTP 200
@pytest.mark.parametrize("run", range(5))
def test_status(page, run):
    response = page.goto(BASE_URL)
    assert response.status == 200, f"Главная страница вернула статус {response.status} вместо 200"








