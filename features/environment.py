import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import config_reader


def before_scenario(context, driver):
    browser_name = config_reader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    time.sleep(25)
    context.driver.get(config_reader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=AttachmentType.PNG)
