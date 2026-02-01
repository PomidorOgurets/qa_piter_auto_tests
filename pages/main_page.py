from playwright.sync_api import Page, expect
from Data.constants import *


class MainPage:
    """Page Object для главной страницы сайта"""

    def __init__(self, page: Page):
        self.page = page

        # Локаторы элементов (с использованием констант)
        self.street_input = page.get_by_role("combobox", name=INPUT_STREET_LABEL)
        self.house_input = page.get_by_role("combobox", name=INPUT_HOUSE_LABEL)
        self.find_tariffs_button = page.get_by_role("button", name=BUTTON_FIND_TARIFFS)
        self.phone_input = page.get_by_role("textbox", name=INPUT_PHONE_LABEL)
        self.show_results_button = page.get_by_role("button", name=BUTTON_SHOW_RESULTS)
        self.view_tariffs_button = page.get_by_role("button", name=BUTTON_VIEW_TARIFFS)
        self.region_link = page.get_by_role("banner").get_by_role("link", name=REGION_DEFAULT)
        self.gatchina_link = page.get_by_role("link", name=REGION_GATCHINA)
        self.gatchina_text = page.get_by_text(REGION_GATCHINA_TEXT, exact=True)

    # ========== Методы для работы с адресом ==========

    def open_main_site(self):
        self.page.goto("https://piter-online.net/")
    def fill_street(self, street_name: str):
        """Заполнить поле улицы"""
        self.street_input.click()
        self.street_input.fill(street_name)
        self.page.get_by_text(street_name).click()
        return self

    def fill_house(self, house_number: str):
        """Заполнить поле дома"""
        self.house_input.fill(house_number)
        self.house_input.press("Enter")
        return self

    def fill_address(self, street: str, house: str):
        """Заполнить полный адрес"""
        self.fill_street(street)
        self.fill_house(house)
        return self

    # ========== Методы для работы с кнопками ==========
    def click_find_tariffs(self):
        """Нажать кнопку 'Найти тарифы'"""
        self.page.wait_for_timeout(1000)
        self.find_tariffs_button.wait_for(state="visible", timeout=TIMEOUT_DEFAULT)
        self.find_tariffs_button.click()
        return self

    def fill_phone(self, phone: str):
        """Заполнить телефон"""
        self.phone_input.fill(phone)
        return self

    def click_show_results(self):
        """Нажать кнопку 'Показать результаты'"""
        self.show_results_button.click()
        return self

    def click_view_tariffs(self):
        """Нажать кнопку 'Смотреть тарифы'"""
        self.view_tariffs_button.wait_for(state="visible", timeout=TIMEOUT_DEFAULT)
        self.view_tariffs_button.click()
        return self

    # ========== Методы для работы с регионом ==========
    def open_region_menu(self):
        """Открыть меню выбора региона"""
        self.region_link.click()
        return self

    def select_gatchina_region(self):
        """Выбрать регион Гатчина"""
        self.gatchina_link.click()
        return self

    # ========== Методы проверок (assertions) ==========
    def expect_tariffs_heading_visible(self, street_name: str):
        """Проверить видимость заголовка с тарифами"""
        heading = self.page.get_by_role("heading",
                                        name=HEADING_TARIFFS_PATTERN.format(street_name=street_name))
        expect(heading).to_be_visible()
        return self

    def expect_gatchina_visible(self):
        """Проверить видимость текста 'Гатчина'"""
        expect(self.gatchina_text).to_be_visible()
        return self

    # ========== Вспомогательные методы ==========
    def goto(self, url: str = BASE_URL):
        """Перейти на страницу"""
        response = self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
        return response

    def fill_complete_form(self, street: str, house: str, phone: str):
        """Заполнить полную форму и получить результаты"""
        (self.fill_address(street, house)
         .click_find_tariffs()
         .fill_phone(phone)
         .click_show_results()
         .click_view_tariffs())
        return self
