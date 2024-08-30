from behave import *
from selenium.webdriver.common.by import By
import random
import string


@given(u'I navigated to Register page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'My Account').click()
    context.driver.find_element(By.LINK_TEXT, 'Register').click()


@when(u'I enter mandatory fields')
def step_impl(context):
    # Generate a random character from the set of all letters (both lowercase and uppercase)
    random_char = random.choice(string.ascii_letters)
    context.driver.find_element(By.ID, 'input-firstname').send_keys('ninja')
    context.driver.find_element(By.ID, 'input-lastname').send_keys('kappa')
    context.driver.find_element(By.ID, 'input-email').send_keys(f'ninjakappa{random_char}@gmail.com')
    context.driver.find_element(By.ID, 'input-telephone').send_keys('11112222')
    context.driver.find_element(By.ID, 'input-password').send_keys('Password@123')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('Password@123')


@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'agree').click()
    context.driver.find_element(By.XPATH, '//*[@value="Continue"]').click()


@then(u'Account should get created')
def step_impl(context):
    expected_text_after_register = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, '//*[@id="content"]/h1').text == expected_text_after_register


@when(u'I enter all fields except email fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('ninja')
    context.driver.find_element(By.ID, 'input-lastname').send_keys('kappa')
    context.driver.find_element(By.ID, 'input-telephone').send_keys('11112222')
    context.driver.find_element(By.ID, 'input-password').send_keys('Password@123')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('Password@123')


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('sukamadrick@gmail.com')


@then(u'Proper message should be displayed about using duplicate email')
def step_impl(context):
    duplicate_email_warning_msg = "Warning: E-Mail Address is already registered!"
    assert (context.driver.find_element(By.XPATH, '//*[@class="alert alert-danger alert-dismissible"]').text ==
            duplicate_email_warning_msg)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    # nothing to do here so simply using pass
    pass


@then(u'Proper message should be displayed about mandatory fields')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,
                                       '//*[@id="account"]/div[2]/div/div').text == 'First Name must be between 1 and 32 characters!'
    assert context.driver.find_element(By.XPATH,
                                       '//*[@id="account"]/div[3]/div/div').text == 'Last Name must be between 1 and 32 characters!'
    assert context.driver.find_element(By.XPATH,
                                       '//*[@id="account"]/div[4]/div/div').text == 'E-Mail Address does not appear to be valid!'
    assert context.driver.find_element(By.XPATH,
                                       '//*[@id="account"]/div[5]/div/div').text == 'Telephone must be between 3 and 32 characters!'
    assert context.driver.find_element(By.XPATH,
                                       '//*[@id="content"]/form/fieldset[2]/div[1]/div/div').text == 'Password must be between 4 and 20 characters!'
