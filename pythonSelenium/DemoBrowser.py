from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe")

driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.get("https://www.youtube.com/watch?v=vc0uRyNNgXE")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()