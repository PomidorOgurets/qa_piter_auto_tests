import pytest
from playwright.sync_api import expect
from Data.constants import *
from Data.test_data import *

@pytest.mark.parametrize("run", range(1))
def test_fill_page(page, run):

    page.goto("https://piter-online.net/")
    page.get_by_role("combobox", name=INPUT_STREET_LABEL).click()
    page.get_by_role("combobox", name=INPUT_STREET_LABEL).fill(TEST_STREETS[0])
    page.get_by_text("Тестовая линия").click()
    page.get_by_role("combobox", name=INPUT_HOUSE_LABEL).fill(TEST_HOUSES[0])
    page.get_by_role("combobox", name=INPUT_HOUSE_LABEL).press(ENTER)

    page.wait_for_timeout(1000)
    page.get_by_role("button", name=BUTTON_FIND_TARIFFS).wait_for(state="visible", timeout=TIMEOUT_DEFAULT)
    page.get_by_role("button", name=BUTTON_FIND_TARIFFS).click()

    page.get_by_role("textbox", name=INPUT_PHONE_LABEL).fill(TEST_PHONES[0])
    page.get_by_role("button", name=BUTTON_SHOW_RESULTS).click()


    page.get_by_role("button", name=BUTTON_VIEW_TARIFFS).wait_for(state="visible", timeout=TIMEOUT_DEFAULT)
    page.get_by_role("button", name=BUTTON_VIEW_TARIFFS).click()


    expect(page.get_by_role("heading", name=HEADING_TARIFFS_PATTERN)).to_be_visible()


@pytest.mark.parametrize("run", range(1))
def test_change_region(page, run):
    page.goto("https://piter-online.net/")
    page.get_by_role("banner").get_by_role("link", name=REGION_DEFAULT).click()
    page.get_by_role("link", name=REGION_GATCHINA).click()
    expect(page.get_by_text(REGION_GATCHINA_TEXT, exact=True)).to_be_visible()


@pytest.mark.parametrize("run", range(1))
def test_status(page, run):
    # Переход на главную и проверка HTTP 200
    response = page.goto(BASE_URL)
    assert response.status == 200, f"Главная страница вернула статус {response.status} вместо 200"








