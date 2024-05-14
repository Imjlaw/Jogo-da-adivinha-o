from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurações
youtube_link = "https://www.youtube.com/watch?v=xV1rmGbzOEQ"
tiktok_username = "D.Imjlaw"
tiktok_password = "Juju2510#"

# Configuração do driver do Chrome
chrome_driver_path = r"C:\Users\Jilso\OneDrive\Área de Trabalho\desafiospurple\chromedriver\chromedriver.exe"

# Configuração do serviço do Chrome
service = Service(chrome_driver_path)
service.start()

# Configuração das opções do navegador
options = webdriver.ChromeOptions()

try:
    # Inicializando o driver do Chrome com as opções configuradas
    driver = webdriver.Chrome(service=service, options=options)

    # Abrindo o site de corte de vídeos
    driver.get("https://www.veed.io/pt-PT/ferramentas/cortador-de-video?utm_id=21022725590&utm_term=&utm_campaign=x_PT_BR-PT-Pmax-New_Customers&utm_source=google&utm_medium=cpc&utm_content=_&hsa_acc=2332311570&hsa_cam=21022725590&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwlZixBhCoARIsAIC745CFFS1diIpSIpH7q797Ac7ah38j4lZ4AM5L0W5l5HDhDWVBLvehntoaAuAFEALw_wcB")

    # Inserindo o link do YouTube e clicando no botão de cortar
    youtube_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "youtube-link-input"))
    )
    youtube_input.send_keys(youtube_link)
    youtube_input.send_keys(Keys.RETURN)

    # Esperando o vídeo ser processado
    time.sleep(10)

    # Obtendo o link do vídeo cortado
    video_link = driver.find_element(By.ID, "video-link").get_attribute("value")

    # Fazendo login no TikTok
    driver.get("https://www.tiktok.com/login")
    driver.find_element(By.NAME, "username").send_keys(tiktok_username)
    driver.find_element(By.NAME, "password").send_keys(tiktok_password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    time.sleep(5)

    # Publicando o vídeo no TikTok
    driver.get("https://www.tiktok.com/upload")
    driver.find_element(By.CSS_SELECTOR, ".upload-video-input").send_keys(video_link)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".post-create-btn").click()
    time.sleep(5)

finally:
    driver.quit()
    service.stop()
