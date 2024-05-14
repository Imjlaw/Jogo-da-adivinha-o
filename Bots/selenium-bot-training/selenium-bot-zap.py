from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Abrir o Chrome e ir direto para a Twitch
driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/")


time.sleep(2)


# Achar o botão de iniciar sessão na Twitch
iniciar_sessao = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button').click()

time.sleep(2)

# Preencher o login e senha
login = driver.find_element(By.ID, "login-username")
login.clear
login.send_keys("Imjlaw")

time.sleep(2)

senha = driver.find_element(By.ID, "password-input")
senha.clear
senha.send_keys("82*Bbg3$ejTt!S7nzvn&ekeB7HdQ^ZFEBFCY!MCz2czwT5BBx8rPJTgQ9kJW")
senha.send_keys(Keys.RETURN)

time.sleep(500)








time.sleep(5)