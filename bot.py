from selenium import webdriver #need for run Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from venv import cred

#create instance of browser using file webdriver for chrome
service = Service(r'.\chromedriver')
browser = webdriver.Chrome(service=service)

#fullscreen
browser.maximize_window()
#get URL for enter websites page in a specific route
browser.get("https://www.linkedin.com/login")


i_email = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((
    By.ID, 
    'username'
    ))
)
i_email.send_keys(cred.camilo.email)

i_pass = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((
    By.ID, 
    'password'
    ))
)
i_pass.send_keys(cred.camilo.password)

b_log = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((
    By.XPATH, 
    "//button[@type='submit']"
    ))
)
b_log.click()

b_search = WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((
    By.XPATH, 
    "//input[@placeholder='Pesquisar']"
    ))
)
b_search.send_keys("RPA")
b_search.send_keys(Keys.RETURN)


b_chat = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((
    By.XPATH,
     "//h3[text()[contains(., 'Danilo Alves')]]",
    ))
)
b_chat.click()

chat_box = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((
    By.XPATH,
     "//div[@aria-label='Escreva uma mensagem']",
    ))
)
chat_box.click()
chat_box.send_keys('Olá Danilo, sou um Bot feito por Ashmeel para te mandar uma mensagem de boa noite! Lembre-se qualquer problema resolvemos na "Oração", Fique com Deus.')

bt_send = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((
    By.XPATH,
     "//button[@type='submit']",
    ))
)
bt_send.click()

bt_slot = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((
    By.XPATH,
     "//button[text()[contains(., 'Vagas')]]",
    ))
)
bt_slot.click()


#force continue running
input('')