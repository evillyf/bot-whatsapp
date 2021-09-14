#!/usr/bin/env python
# coding: utf-8

# # Objetivo: Enviar mensagem para várias pessoas ou grupos automaticamente

# ### Cuidados!
# 
# 1. Whatsapp não gosta de nenhum tipo de automação
# 2. Isso pode dar merda, já to avisando
# 3. Isso não é o uso da API oficial do Whatsapp, o próprio whatsapp tem uma API oficial. Se o seu objetivo é fazer envio em massa ou criar aqueles robozinhos que respondem automaticamente no whatsapp, então use a API oficial
# 4. Meu objetivo é 100% educacional

# ### Dito isso, bora automatizar o envio de mensagens no Whatsapp
# 
# - Vamos usar o Selenium (vídeo da configuração na descrição)
# - Temos 1 ferramenta muito boa alternativas:
#     - Usar o wa.me (mais fácil, mais seguro, mas mais demorado)

# In[3]:


import pandas as pd

contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)


# In[4]:


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


# já estamos com o login feito no whatsapp web
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


# In[ ]:




