from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.instagram.com/")
time.sleep(3)
navegador.find_element(By.NAME, 'username').send_keys("YOUR ACCOUNT")

time.sleep(5)
navegador.find_element(By.NAME, 'password').send_keys("YOUR PASSWORD")
time.sleep(5)
navegador.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
time.sleep(5)

navegador.find_element(By.XPATH, '//button[text()="Agora não"]').click()
time.sleep(5)
navegador.find_element(By.XPATH, '//button[text()="Agora não"]').click()
time.sleep(10)


# navegador.find_element(By.CSS_SELECTOR, '[type="button"]').click()
