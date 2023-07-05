from .locators import Basket
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_has_no_products(self):
        assert self.is_not_element_present(*Basket.BASKET_ITEMS)

    def basket_has_message_about_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*Basket.MESSAGE_ABOUT_EMPTY).text
