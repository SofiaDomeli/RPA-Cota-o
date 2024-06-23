from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import psycopg2

# Variáveis

data_ori = datetime.now()

# Pegando o valor do dolar

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.google.com/finance/quote/USD-BRL')
sleep(1)

dolar = float(driver.find_element(By.CLASS_NAME, 'fxKbKc').text)
data = str(data_ori.strftime('%Y-%m-%d'))
hora = str(data_ori.strftime('%H:%M'))

driver.quit()

print(dolar)
