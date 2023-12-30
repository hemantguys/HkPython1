from  selenium import  webdriver
import time

from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
driver.delete_all_cookies()

time.sleep(2)
LinkCount=driver.find_elements(By.TAG_NAME,'a')

time.sleep(2)

for i in LinkCount:
    print(i.text)

print("Total Links = ", len(LinkCount))

