from playwright.sync_api import Page
import dataclasses
@dataclasses.dataclass
class Address:
    street: str
    house: int


address = Address("Тестовая", 1)