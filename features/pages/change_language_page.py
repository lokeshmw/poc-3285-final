import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class Change_language(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    language_option_xpath = "//div/a[@id='icp-nav-flyout']/span/span[@class='nav-line-2']/span[@class='nav-icon nav-arrow']"
    all_language_xpath = "//div[@class='a-column a-span7']/div[@class='a-row a-spacing-mini']"
    confirm_xpath = "//input[@aria-labelledby='icp-save-button-announce']"
    verify_language_xpath = "//div/a[@id='icp-nav-flyout']/span/span[@class='nav-line-2']"

    def click_language_option(self):
        self.click_on_element(" language_option_xpath", self.language_option_xpath)

    def change_language(self):
        languages = self.get_elements("all_language_xpath", self.all_language_xpath)
        for i in languages:
            if "HI" in i.text:
                i.click()
        self.click_on_element("confirm_xpath", self.confirm_xpath)

    def verify_language(self):
        self.driver.refresh()
        a = self.get_element("verify_language_xpath", self.verify_language_xpath).text
        print(a)
        return a

