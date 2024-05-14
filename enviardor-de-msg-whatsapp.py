from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Defina a variável driver globalmente
driver = None

try:
    # Inicialização do serviço do Chrome WebDriver
    service = Service(r'C:\Users\Jilso\OneDrive\Área de Trabalho\desafiospurple\chromedriver\chromedriver.exe')

    # Inicialização do Driver do Chrome com opções explícitas
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")  # Desabilita as notificações
    driver = webdriver.Chrome(service=service, options=options)

    # Abre o WhatsApp web
    driver.get('https://web.whatsapp.com')
    time.sleep(10)

    # Encontrando o campo de pesquisa
    search_box = driver.find_element_by_xpath(r'/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/p')

    # Digita o nome do contato ou grupo
    search_box.send_keys("Isa")
    search_box.send_keys(Keys.ENTER)

    # Espera um momento para carregar a conversa
    time.sleep(2)

    # Encontra o campo de mensagem e envia a mensagem
    message_box = driver.find_element_by_xpath(r'/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_box.send_keys("Abcde")
    message_box.send_keys(Keys.ENTER)

except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    # Verifique se o driver foi inicializado antes de tentar fechar
    if driver:
        # Fecha o navegador
        driver.quit()
