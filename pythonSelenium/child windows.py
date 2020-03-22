from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()

print(driver.find_element_by_tag_name("h3").text)
childvariable=driver.window_handles[1]  #stpre the child windows id in variable
driver.switch_to.window(childvariable) #pass the child window id
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)