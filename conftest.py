import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser...')
    chrome_options = Options()
    chrome_options.add_argument('--maximized')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver_path='C:/chromedriver/chromedriver_python.exe'

    browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    yield browser

    print('\nquit browser...')
    browser.quit()
