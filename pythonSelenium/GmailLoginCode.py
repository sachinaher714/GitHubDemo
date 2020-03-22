
from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.maximize_window()
driver.find_element_by_css_selector("#identifierId").send_keys("sachindip2012@gmail.com")
driver.find_element_by_css_selector(".RveJvd").click()

#driver.find_element_by_xpath("//input[@type='password']").send_keys("01051962") #or- using xpath
driver.find_element_by_css_selector("input[class='whsOnd zHQkBf']").send_keys("01051962")
driver.find_element_by_css_selector("span[class='RveJvd snByac']").click()
driver.close()


