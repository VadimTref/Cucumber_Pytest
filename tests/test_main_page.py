import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_link_to_product_page()
    page.go_to_product_page()


@pytest.mark.regression
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    page = LoginPage(browser, link)
    page.should_be_login_page()


def test_user_сan_autorize(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open_page()
    page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    page.should_be_autorized_user()
