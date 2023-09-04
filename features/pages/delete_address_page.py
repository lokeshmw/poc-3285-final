from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class Delete_address(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_xpath = "//a[contains(.,'Hello, Lokesh.M')]"
    click_address_xpath = "//h2[normalize-space()='Your Addresses']"
    all_address_xpath = "//div[@class ='a-row a-spacing-micro']/div/div"
    address_name_xpath = "//div[@class ='a-row a-spacing-micro']/div/div/div/div/div/ul/li[1]"
    remove_address_xpath = "//div[@class ='a-row a-spacing-micro']/div/div/span/a[text()='Remove']"
    yes_delete_xpath = "//div[@class ='a-popover-inner']/div[@class='a-section']/div[4]/div[2]/div/div[@class='a-column a-span8']"
    deleted_text_xpath = "//h4[.='Address deleted']"

    def click_account(self):
        self.click_on_element("account_xpath", self.account_xpath)

    def click_address(self):
        self.click_on_element("click_address_xpath", self.click_address_xpath)

    def delete_address_(self):
        addresses = self.get_elements("address_name_xpath", self.address_name_xpath)
        for x in addresses:
            if x.text == "Lokesh.M":
                self.click_on_element("remove_address_xpath", self.remove_address_xpath)
                self.click_on_element("yes_delete_xpath", self.yes_delete_xpath)

