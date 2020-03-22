validatetext="option3"
from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()
alert=driver.switch_to.alert
alerttext=alert.text
#print(alerttext)
assert validatetext in alerttext
alert.accept()   #positive i.e. to select ok/yes option
driver.find_element_by_id("confirmbtn").click()
alert=driver.switch_to.alert
alerttext=alert.text
print(alerttext)
alert.dismiss()  #for negative i.e for to select cancel/no option