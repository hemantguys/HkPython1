import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://selenium.dev")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(5)

driver.quit()