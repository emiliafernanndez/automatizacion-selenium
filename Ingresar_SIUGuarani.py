from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://autogestion.frcu.utn.edu.ar/autogestion/")

# DATOS CUENTA
usuario="";
clave="";

time.sleep(5)
usuario= driver.find_element(By.ID, 'usuario')
usuario.send_keys(usuario)

contraseña=driver.find_element(By.ID, "password")
contraseña.send_keys(clave+Keys.ENTER)

time.sleep(3)

driver.quit()