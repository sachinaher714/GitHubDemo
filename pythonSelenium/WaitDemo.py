#implicit wait- this is applied to every step in program
#explicit wait- appliaed to specific step in program

import time

from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.implicitly_wait(4)  #wait untill 5 second  if object is not displayed
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

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click() #css from classname
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
