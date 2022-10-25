from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_empty()
        self.should_be_text()

    def should_be_empty(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT), 'The product is present'

    def should_be_text(self):
        assert len(self.browser.find_element(*BasketPageLocators.TEXT).text), 'The text is missing'
