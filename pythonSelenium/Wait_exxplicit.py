import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))

assert count== 3
items=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for item in items:
    item.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='cart-preview active']/div[2]").click() #or
#driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click() #using xpath locator bases on text
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click() #css from classname
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

