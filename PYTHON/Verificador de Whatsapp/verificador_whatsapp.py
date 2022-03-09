from selenium import webdriver
from time import sleep
celular = input("\n\nInvestigador de Whastapp: ")
navegador = webdriver.Chrome()
navegador.get('https://api.whatsapp.com/send?1=pt_BR&phone=550'+celular)
navegador.find_element_by_xpath('//*[@id="action-button"]').click()
sleep(1)
navegador.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
