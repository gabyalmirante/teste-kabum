from selenium import webdriver
from time import sleep
from config import Config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

#Desabilitar popup de notificações do site 
option = Options()
option.add_argument('--disable-notifications')
driver = webdriver.Chrome(chrome_options= option)
#Configuração de valores-chave
config = Config()

def buscar_notebook(driver):
    #Acessanado o site da kabum
    try:
        driver.get(config.URL)
        #Tentando fechar o consentimento de cookies, só prosseguir quando fechar
        try:
            driver.find_element_by_id('onetrust-accept-btn-handler').click()
        except:
            pass
        sleep(3)
        #Acessando a barra de busca do site ele aparece tanto a busca inteligente quanto busca norma, mudando o seu id;
        #Realizando a busca da kabum tanto para busca inteligente quando para busca normal
        try:
            elem = driver.find_element_by_id('smarthint-search-input')
            elem.send_keys('notebook')
            elem2 = driver.find_element_by_id('smarthint-search-input')
            elem2.send_keys(Keys.RETURN)
            sleep(3)
            driver.find_element_by_xpath("//div[@id='secaoOfertasCampanhaSh']/div[2]/div/div/div[1]/div/a").click()
            pass
        except:
            elem = driver.find_element_by_id('input-busca')
            elem.send_keys('notebook')
            sleep(2)
            driver.find_element_by_xpath("//div[@id='barraBuscaKabum']/div/div/div[1]/div/div[2]").click()
            pass
        sleep(3)
        #Guardando o nome do primeiro produto clicado para futura verificação
        nome_produto = driver.find_element_by_xpath("//div[@id='__next']/main/article/section/div[2]/h1").text
        #Calculando frete
        frete = driver.find_element_by_id('inputCalcularFrete')
        frete.click()
        frete.send_keys(config.CEP)
        #Exibindo valores dos fretes por 3 segundos
        driver.find_element_by_id('botaoCalcularFrete').click()
        sleep(3)
        #Fechando valores dos fretes
        driver.find_element_by_xpath("//div[@data-testid='btnClose']").click()
        sleep(2)
        #Adicionando produto ao carrinho
        driver.find_element_by_xpath("//button[contains(text(), 'COMPRAR')]").click()
        sleep(2)
        #Guardando nome do produto que está no carrinho para verificação
        nome_produto_carrinho = driver.find_element_by_class_name('productName').text
        #Realizando a verificação do produto; conferir se o produto clicado inicialmente é o mesmo do produto do carrinho 
        if nome_produto == nome_produto_carrinho:
            print("Produto validado!")
        else:
            print("Produto Incorreto!")
        sleep(2)
        driver.quit()

    #Caso dê algum erro no meio do caminho, exibir erro e fechar navegador
    except Exception as e:
        print(e)
        try:
            driver.quit()
        except:
            pass
buscar_notebook(driver)
