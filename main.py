from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") 

driver = webdriver.Chrome(options=options)

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

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2) 
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2) 
print("Desplazamiento completado.")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Documentation"))
)

try:
    doc_link = driver.find_element(By.LINK_TEXT, "Documentation")
    doc_link.click()
    print("Accediendo a la documentación.")
except Exception as e:
    print(f"No se pudo encontrar el enlace de 'Documentation': {e}")

time.sleep(3)
driver.quit()