
import pandas as pd

contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)





from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import urllib
import os 


#Mantém o whatsapp aberto 
dir_path = os.getcwd() #pega local do .pi
profile = os.path.join(dir_path, "profile", "wpp") #cria as pastas para armazenar os cookies
options = Options()
options.add_argument(r"user-data-dir={}".format(profile))
#options.add_argument("--headless") #modo oculto do chrome
navegador = webdriver.Chrome(options=options)
navegador.get('https://web.whatsapp.com/')
while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(3)


# fazer login uma vez no whatsapp web depois ficará armazenado
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER) #xpath do texto
    time.sleep(10)
     
navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys('Estácio T.I') #clicar na barra de pesquisa de contatos e procurar o grupo
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span').click() #clicar na conversa do grupo (peguei o xpath do nome do grupo)
navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys('Oi! Testando automação 123 kk') #envia o texto no campo de mensagem
navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER) #xpath do texto






