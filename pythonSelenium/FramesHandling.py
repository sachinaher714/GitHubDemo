import time
#if tag name is iframe,frame ,frameset then this will be frame and we have to switch from html to frame
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element_by_link_text("iFrame").click()
time.sleep(5)
driver.switch_to.frame("mce_0_ifr") #pass the frame id/frame name/frame index to switch to frame mode
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("able to edit box")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)