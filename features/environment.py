from selenium import webdriver


def before_scenario(context, driver):
    """
    This function work as a setup function before scenario execution.
    """
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tutorialsninja.com/demo/')


def after_scenario(context, driver):
    """
    This function work as a teardown function after scenario execution.
    """
    context.driver.quit()
