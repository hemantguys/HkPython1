import time

from  selenium import  webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)
driver.close()git 