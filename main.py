import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/ref=nav_logo")
time.sleep(20)
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_ya_signin']").click()
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(8105000676)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Loki@1234")
driver.find_element(By.ID, "auth-signin-button").click()
driver.find_element(By.XPATH, "//div/a[@id='icp-nav-flyout']/span/span[@class='nav-line-2']/span[@class='nav-icon nav-arrow']").click()
languages = driver.find_elements(By.XPATH, "//div[@class='a-column a-span7']/div[@class='a-row a-spacing-mini']")
for i in languages:
    if "EN" in i.text:
        i.click()
driver.find_element(By.XPATH, "//input[@aria-labelledby='icp-save-button-announce']").click()
time.sleep(10)
driver.refresh()
time.sleep(20)
a = driver.find_element(By.XPATH, "//div/a[@id='icp-nav-flyout']/span/span[@class='nav-line-2']").text
print(a)
