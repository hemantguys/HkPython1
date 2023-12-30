import time

from selenium import  webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("C:\\browerdriver\\chromedriver.exe")

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


driver.get("https://google.com")

print(driver.title)
print(driver.current_url)

time.sleep(5)

driver.close()