from  selenium import  webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.maximize_window()

#Enter email id
Webelement_Email=driver.find_element(By.XPATH,"//input[contains(@id,'email')]")
Webelement_Email.send_keys("hemantkumar@yahoo.in")

time.sleep(1)
#Enter password
Webelement_Password = driver.find_element(By.ID, 'pass')
Webelement_Password.send_keys("Hk9815925959")

#Click Login button

time.sleep(2)
Webelement_LoginButton = driver.find_element(By.PARTIAL_LINK_TEXT,'Log in')
Webelement_LoginButton.click()

time.sleep(5)
driver.quit()