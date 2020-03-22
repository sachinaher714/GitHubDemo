from select import select
from time import sleep
from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkbox=driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkbox))
for each in checkbox:
    if each.get_attribute("value")== "option2":
        each.click()
        assert each.is_selected() #to check if check boxes are select or not if not then assrt the


radiobuttons = driver.find_elements_by_css_selector("input[name='radioButton']")  #store all web elements into list
print(len(radiobuttons))
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
dropdown=select(driver.find_element_by_css_selector("select[id*='dropdown']"))
dropdown.select_by_visible_text("Option1")