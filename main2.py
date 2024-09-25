from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://google.com")
      
WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Selenium" + Keys.ENTER)
      
WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium"))
)
      
driver.save_screenshot('resultados_busqueda.png')
      
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
link.click()

WebDriverWait(driver, 5).until(
     EC.title_contains("Selenium")
)

print("El título de la página es correcto:", driver.title)

time.sleep(5)
driver.quit()
