from playwright.sync_api import Page, expect
from Data.constants import *


"""Page Object для главной страницы сайта"""
class MainPage:

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


    # Открыть главную страницу
    def open_main_site(self):
        self.page.goto(BASE_URL)

    # Заполнить поле улицы
    def fill_street(self, street_name: str):
        self.street_input.click()
        self.street_input.fill("Тес")
        self.page.get_by_text("Ленинградская область, Хвойный").click()
        return self

    # Заполнить поле дома
    def fill_house(self, house_number: str):
        self.house_input.fill(house_number)
        self.house_input.press(ENTER)
        return self

    # Заполнить полный адрес
    def fill_address(self, street: str, house: str):
        self.fill_street(street)
        self.fill_house(house)
        return self

    # Нажать кнопку 'Найти тарифы'
    def click_find_tariffs(self):
        self.page.wait_for_timeout(1000)
        self.find_tariffs_button.wait_for(state="visible", timeout=TIMEOUT_DEFAULT)
        self.find_tariffs_button.click()
        return self

    # Заполнить телефон
    def fill_phone(self, phone: str):
        self.phone_input.fill(phone)
        return self

    # Нажать кнопку 'Показать результаты'
    def click_show_results(self):
        self.show_results_button.click()
        return self

    # Нажать кнопку 'Смотреть тарифы'
    def click_view_tariffs(self):
        self.view_tariffs_button.wait_for(state="visible", timeout=TIMEOUT_DEFAULT)
        self.view_tariffs_button.click()
        return self

    # Открыть меню выбора региона
    def open_region_menu(self):
        self.region_link.click()
        return self

    # Выбрать регион "Гатчина"
    def select_gatchina_region(self):
        self.gatchina_link.click()
        return self

    # Проверить видимость заголовка с тарифами
    def expect_tariffs_heading_visible(self):
        heading = self.page.get_by_role("heading",
                                        name=HEADING_TARIFFS_PATTERN)
        expect(heading).to_be_visible()
        return self

    # Проверить видимость текста 'Гатчина'
    def expect_gatchina_visible(self):
        expect(self.gatchina_text).to_be_visible()
        return self

    # Полное заполнение заявки + переходы по сайту по нажатию по кнопкам.
    def fill_complete_form(self, street: str, house: str, phone: str):
        (self.fill_address(street, house)
         .click_find_tariffs()
         .fill_phone(phone)
         .click_show_results()
         .click_view_tariffs())
        return self
