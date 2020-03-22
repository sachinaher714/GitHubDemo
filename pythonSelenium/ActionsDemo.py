import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
#ActionChains class
action=ActionChains(driver)
time.sleep(4)
action.move_to_element(driver.find_element_by_xpath("//nav[@id='primaryNav']/div[2]/button")).click().perform()
driver.find_element_by_link_text("Genealogies").click()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

print(driver.find_element_by_id("displayed-text").is_selected())
driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_id("displayed-text").is_selected())

#action.double_click(driver.find_element_by_id("locator path")
#action.context_click(driver.find_element_by_id((locator)))- this is for right click

