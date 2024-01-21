from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_TO_PRODUCT_PAGE = (By.XPATH, "//ul[@id='browse']//ul//a")
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')
    WELCOME = (By.CSS_SELECTOR, "//h2")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, "//form[@id='register_form']//button")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class ProductsPageLocators:
    H2_TITLE = (By.XPATH, "//h1")
