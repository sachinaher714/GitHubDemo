from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("sachin")
print(driver.find_element_by_name("name").text)

print(driver.find_element_by_name("name").get_attribute("value")) #to print text which selenium script send
print(driver.execute_script('return document.getElementsByName("name")[0].value')) #using java script dom-document object model

shopbutton=driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script('arguments[0].click();', shopbutton)  #to click using java script

driver.execute_script("window.scrollTo(0,200);")  #to scroll down the window using java script, pass arguments as height of the wab page

