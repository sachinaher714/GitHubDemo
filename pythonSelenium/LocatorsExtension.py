from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
#river.find_element_by_css_selector("input[type='email']").send_keys("myname") #or

driver.find_element_by_css_selector("#username").send_keys("cool")#fastest css using id

#driver.find_element_by_xpath("//input[@id='username']").send_keys("aher")

driver.find_element_by_css_selector(".password").send_keys("12345") #css using classname
#driver.find_element_by_css_selector("#username").clear()
#driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()# xpath based on text

print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)#xpath by traversing parent tag to child-to print username text
print(driver.find_element_by_css_selector("div[id='usernamegroup'] label").text)#css using traversing parent tag to child -printusername text
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text) #xpath grand parent to child tag->tp print username text
print(driver.find_element_by_xpath("//form[@name='login']/label").text)#xpath by traversing grand parent to child tag-print password tag
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)#css by traversing grand parent to child tag-print password text

driver.find_element_by_xpath("//form[@name='login']/div[3]/input").click() #xpath by traversing from grand tag to chile tag->to click on remember me check box