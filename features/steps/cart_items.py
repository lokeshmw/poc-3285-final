from behave import *

from features.pages.get_cart_items_page import cart_items
from features.pages.home_page import HomePage


@given(u'I logged my account and got navigated to the the Homepage')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()
    time.sleep(20)
    context.login_page.enter_phone("8105000676")
    context.login_page.enter_password("Loki@1234")
    context.verify_login = context.login_page.click_on_login()


@when(u'I clicked on cart option')
def step_impl(context):
    context.cart_items = cart_items(context.driver)
    context.cart_items.click_cart()


@when(u'printed the items present in cart')
def step_impl(context):
    context.cart_items.get_cart_items()
