#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

import numpy as np
import pandas as pd
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests

#Selenium Options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

#Variaveis para execucao
baseurl = "http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?idioma=pt-br"
btnId = 'ctl00$contentPlaceHolderConteudo$BuscaNomeEmpresa1$btnTodas'
clickTimeout = 10
timeSleep = 5


headerxpath = "//*[@id='ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01']//thead//tr//*"
tablexpath = "//*[@id='ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01']//tr//td"
linkxpath = "//*[@id='ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01']//tr//td//a"

#driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/lib/chromium/chromedriver')
driver = webdriver.Chrome(chrome_options=options)

driver.get(baseurl)

allbtn = driver.find_element_by_name(btnId)
assert allbtn is not None

allbtn.click()

print("Pagina carregada! Buscando Header")

#Encontra o botão que lista todas as empresas
header = []
for i in range(clickTimeout):

    header = [elem.text for elem in driver.find_elements_by_xpath(headerxpath)]

    if header:
        break

    print("Header vazio, tentando novamente")

    time.sleep(timeSleep)

print("Carregando tabela")

table = [elem.text for elem in driver.find_elements_by_xpath(tablexpath)]

#Transforma a lista numa matriz de 3 colunas
table = np.array(table).reshape(-1, 3)

print("Carregando Links")

links = [
    elem.get_attribute("href")
    for elem in driver.find_elements_by_xpath(linkxpath)
]

driver.close()

#O link existe em duas colunas da tabela então ele aparece igual em 2 linhas, aqui removo as linhas pares
links = links[::2]
codigoCVM = [ link.split('=')[1] for link in links ]

#Gera um dataframe pandas
tableDf = pd.DataFrame(table, columns=header)

# Adiciona novas colunas à tablea      
tableDf['Link'] = links
tableDf['CodigoCVM'] = codigoCVM

# tableDf['CodigoCVM'] = tableDf['Link'].str.split("=", 1)

print("Dados recuperados")
print(tableDf)
print(tableDf['Link'][0])
req = requests.get(tableDf['Link'][0])
print(req.content)
