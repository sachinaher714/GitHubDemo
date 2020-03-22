from selenium import webdriver

chrome_option=webdriver.ChromeOptions()

chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")  #execution run at backend i.e. chrome window will not open
chrome_option.add_argument("--ignore-certification-errors")

driver = webdriver.Chrome(executable_path="D:\\Photos\\chromedriver.exe",options=chrome_option)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)