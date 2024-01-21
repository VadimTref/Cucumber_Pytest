from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductsPageLocators


class MainPage(BasePage):

    def should_be_link_to_product_page(self):
        assert self.element_is_present(*MainPageLocators.LINK_TO_PRODUCT_PAGE)

    def should_be_main_page(self, expected_text):
        assert self.browser.find_element(*MainPageLocators.WELCOME) == expected_text

    def should_be_products_page(self, expected_text):
        assert self.browser.find_element(*ProductsPageLocators.H2_TITLE) == expected_text

    def go_to_product_page(self):
        self.browser.find_element(*MainPageLocators.LINK_TO_PRODUCT_PAGE).click()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()
