from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        product_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        product_add.click()
    
    def should_be_product_page(self):
        self.should_be_name_add_product()
        self.should_be_price_add_product()

    def should_be_name_add_product(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text == self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text, \
        'The name does not match'

    def should_be_price_add_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text == self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text, \
        'The price does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Success message is presented, but should not be'

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        'The element does not disappear, but it should disappear'
