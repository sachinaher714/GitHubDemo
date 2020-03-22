# this is program to 1>check selected vegatables on page 1 are correctly displayed on next page2  2>check if discount prize is decresed or not
#3>cross total check out amt with total amount

import time

list = []
list1 = []
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
# vegetables=driver.find_elements_by_css_selector("h4[class='product-name']")
# for i in vegetables:
# print(i.text)

items = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4-this is path to traverse from child to grand
for item in items:
    list.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()
print(list)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='cart-preview active']/div[2]").click()

items1 = driver.find_elements_by_css_selector("p.product-name")
print(len(items1))
for item in items1:
    list1.append(item.text)
print(list1)
assert list != list1
beforecoupn = int(driver.find_element_by_css_selector(".discountAmt").text)
print(beforecoupn)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()  # css from classname

time.sleep(5)
aftercoupn = float((driver.find_element_by_css_selector(".discountAmt").text))
print(aftercoupn)
assert float(aftercoupn) < int(beforecoupn)
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
prizes=[]
sum=0
values=driver.find_elements_by_xpath("//tr/td[5]/p")
for j in values:
    prizes.append(j.text)
print(prizes)

for i in prizes:
    sum=sum+int(i)
print(sum)
print()
#instead of above 2 for loop we can optimize with one code
#for j in values:
 #   sum=sum+int(j.text)
#print(sum)

totamt=int(driver.find_element_by_css_selector(".totAmt").text)
print(totamt)
assert totamt ==sum