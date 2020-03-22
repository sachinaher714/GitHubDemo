import time

list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
print(list)
list1=[]
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
item=(driver.find_elements_by_css_selector("h4.product-name"))
for i in item:
    list1.append(i.text)
print(list1)

assert list1==list


