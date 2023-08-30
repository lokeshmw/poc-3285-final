from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class cart_items(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    cart_xpath = "//span[normalize-space()='Cart']"
    cart_items_xpath = "//form[@id='activeCartViewForm']/div[@data-name='Active Items']/div/div[@class='sc-list-item-content']/div/div[@class='sc-item-content-group']/ul/li/span/a/span/span"

    def click_cart(self):
        self.click_on_element("cart_xpath", self.cart_xpath)

    def get_cart_items(self):
        all_cart_items = self.get_elements("cart_items_xpath", self.cart_items_xpath)
        for i in all_cart_items:
            print(i.text)


