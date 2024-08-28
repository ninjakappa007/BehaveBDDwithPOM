import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigated to home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://tutorialsninja.com/demo/")


@when(u'I enter valid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('HP')


@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()
    context.driver.quit()

@when(u'I enter invalid product into the search box field')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When I enter invalid product into the search box field')


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then Proper message should be displayed in search results')


@when(u'I dont enter anything into the search box field')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When I dont enter anything into the search box field')
