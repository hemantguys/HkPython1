import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

Firefoxdriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
Webelement_Email_ID=driver.find_element(By.XPATH, "//input[@id='Email']")
Webelement_Email_ID.send_keys("keshav1234@gmail.com")

Webelement_password=driver.find_element(By.XPATH, "//input[@id='Password']")
Webelement_password.send_keys("Hk9815925959")

Webelement_LoginButton= driver.find_element(By.XPATH,"//input[@class='button-1 login-button']")
Webelement_LoginButton.click()
time.sleep(3)
driver.quit()

