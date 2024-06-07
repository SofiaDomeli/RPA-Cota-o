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

# Conexão com o database 

conn = psycopg2.connect(
    dbname="defaultdb",
    user="avnadmin",
    password="AVNS_PiPCdU87ySKStvr7N8q",
    host="pg-362da2a-wowk.f.aivencloud.com"
)
 
# Criar um cursor
cur = conn.cursor()
 
# Comando SQL para chamar a stored procedure
comando = "CALL inserir_tabela(%s, %s, %s)"
 
# Argumentos para a stored procedure
args = (data, hora, dolar)
 
# Executar a stored procedure
cur.execute(comando, args)
 
# Confirmar a transação
conn.commit()
 
# Fechar a conexão
cur.close()
conn.close()
