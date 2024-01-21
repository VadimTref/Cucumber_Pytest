# environment.py

from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture
def browser_chrome(context):
    print("Setting up Chrome browser...")
    chrome_options = Options()
    chrome_options.add_argument('--maximized')  # You can customize Chrome options as needed
    driver_path = 'C:/chromedriver/chromedriver_python.exe'
    context.browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    yield context.browser
    print("Tearing down Chrome browser...")
    context.browser.quit()


def before_all(context):
    # This hook runs before all features and scenarios
    print("Executing before_all hook...")
    use_fixture(browser_chrome, context)


def before_feature(context, feature):
    # This hook runs before each feature
    print(f"Executing before_feature hook for {feature.name}")


def before_scenario(context, scenario):
    # This hook runs before each scenario
    print(f"Executing before_scenario hook for {scenario.name}")


def after_scenario(context, scenario):
    # This hook runs after each scenario
    print(f"Executing after_scenario hook for {scenario.name}")


def after_feature(context, feature):
    # This hook runs after each feature
    print(f"Executing after_feature hook for {feature.name}")


def after_all(context):
    # This hook runs after all features and scenarios
    print("Executing after_all hook...")
