from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

new=[]
driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
driver.maximize_window()
#driver.execute_script("window.scrollTo(0,430);")
products=driver.find_elements_by_xpath("//div[@class='card h-100']")
for i in products:
    productName=i.find_element_by_xpath("div/h4/a").text
    if productName=="Nokia Edge":
        var=productName
        i.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
var2=driver.find_element_by_css_selector("h4[class='media-heading']").text
assert var2==var
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[value='Purchase']").click()
print(driver.find_element_by_class_name("alert-success").text)

driver.get_screenshot_as_file("screen.png")
    



