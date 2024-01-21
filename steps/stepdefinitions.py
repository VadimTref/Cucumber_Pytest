from behave import given, when, then
from pages.main_page import MainPage
from environment import browser_chrome
from pages.locators import ProductsPageLocators
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/'


@given("Main page is opened")
def when_user_opens_main_page(browser_chrome):
    browser_chrome.browser.get(link)


@when("User clicks All Products")
def then_main_page_opened(browser_chrome):
    browser_chrome.browser.find_element(*MainPageLocators.LINK_TO_PRODUCT_PAGE).click()


@then("Products page is opened")
def then_product_page_is_opened(browser_chrome):
    assert 'catalogue' in browser_chrome.browser.current_url
