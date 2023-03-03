import undetected_chromedriver as webdriver
import time
from selenium.webdriver.common.by import By
import random 

option = webdriver.ChromeOptions()
profile = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
option.add_argument (f"user-data-dir = {profile}")

driver = webdriver.Chrome (options = option, use_subprocess = True)

driver.get ('https://bateponto.pontotel.com.br/#/')
time.sleep(2)
matriculas = ['0279']

for mat in matriculas:
    pergunta = input('Gostaria de Registrar o Ponto do: ' + mat + '?')
    if pergunta == 'Sim':
        driver.find_element(By.ID , 'senhanumerica').send_keys (mat)
        time.sleep (2)
        
        driver.find_element(By.ID , 'confirmasenhanumerica').click()
        time.sleep (5)

        driver.find_element (By.CLASS_NAME , 'btn-success').click()
        time.sleep (5)

        driver.find_element (By.CLASS_NAME , 'btn3d').click()
        time.sleep (2)
