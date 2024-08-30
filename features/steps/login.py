from behave import *
from selenium.webdriver.common.by import By


@given(u'I navigated to Login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@title='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'I enter valid email and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("sukamadrick@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("11112222")


@when(u'I click login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@value='Login']").click()


@then(u'I should get logged in')
def step_impl(context):
    expected_text_after_login = "Logout"
    assert context.driver.find_element(By.LINK_TEXT, "Logout").text == expected_text_after_login


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("sukamadrick69@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("11112222")


@then(u'I should get proper error message')
def step_impl(context):
    # Here i am adding two expected text because if we are running this test for multiple iterations we might get second text
    expected_text_if_login_failed = "Warning: No match for E-Mail Address and/or Password."
    expected_text_if_login_failed_2 = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
    assert (context.driver.find_element(By.XPATH,
                                        '//*[@id="account-login"]/div[1]').text == expected_text_if_login_failed or
            context.driver.find_element(By.XPATH,
                                        '//*[@id="account-login"]/div[1]').text == expected_text_if_login_failed_2)


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("sukamadrick@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("111122223333")


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("sukamadrick69@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("111122223333")


@when(u'I enter nothing into email and password field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
