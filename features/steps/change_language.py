import time

from behave import *

from features.pages.change_language_page import Change_language
from features.pages.home_page import HomePage


@given(u'I logged to my account and got navigated to Homepage')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()
    time.sleep(20)
    context.login_page.enter_phone("8105000676")
    context.login_page.enter_password("Loki@1234")
    context.verify_login = context.login_page.click_on_login()


@when(u'I clicked on language option')
def step_impl(context):
    context.change_address = Change_language(context.driver)
    context.change_address.click_language_option()


@when(u'changed the language to what is requested')
def step_impl(context):
    context.change_address.change_language()


@Then('verify the changed language')
def step_impl(context):
    assert "EN" in context.change_address.verify_language()
