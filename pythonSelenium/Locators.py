from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("input[name='name']").send_keys("sachin")
#driver.find_element_by_class_name("form-control ng-pristine ng-invalid ng-touched").send_keys("sachin")
driver.find_element_by_name("email").send_keys("sachindip2012@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("12345")
driver.find_element_by_id("exampleCheck1").click()
dropdown=Select(driver.find_element_by_id("exampleFormControlSelect1"))#need to create opject to handdle dropdown box
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_id("in""lineRadio2").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
#driver.find_element_by_xpath("//input[@class='btn btn-success']").click()

#print(driver.find_element_by_class_name("alert-success").text)
message= driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
#print(driver.find_element_by_css_selector("div[class='alert-success']").text)
assert "success" in message #to check test is pass/fail