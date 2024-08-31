from selenium import webdriver
from utilities import config_reader


def before_scenario(context, driver):
    """
    This function work as a setup function before scenario execution.
    """
    browser_name = config_reader.read_config('basic info', 'browser')
    if browser_name.lower() == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser_name.lower() == 'firefox':
        context.driver = webdriver.Firefox()

    context.driver.get(config_reader.read_config('basic info', 'url'))


def after_scenario(context, driver):
    """
    This function work as a teardown function after scenario execution.
    """
    context.driver.quit()
