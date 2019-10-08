#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

from database import DBase as db
from table import Table
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
N_CLUSTERS = 20

url = "https://fundamentus.com.br/resultado.php"
# data to be sent to api
data = {
    'Cookie':
    "_fbp=fb.2.1565444298540.1134836130; __utma=138951332.783964612.1565444298.1565447188.1565449124.3; __utmb=138951332.4.10.1565449124; __utmc=138951332; __utmz=138951332.1565444298.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; PHPSESSID=61rls69m006n47fhdlrdnvbqs2",
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Orign': "https://fundamentus.com.br",
    'Content-Length': "471",
    'Accept-Language': 'pt-br',
    'Host': 'fundamentus.com.br',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
    'Referer': 'https://fundamentus.com.br/buscaavancada.php',
    'Accept-Encoding': 'br, gzip, deflate',
    'Connection': 'keep-alive'
}

table = Table(url, data)
fileName = "fundamentus_" + str(datetime.datetime.now()) + ".csv"
df = table.get()
labels = list(df[ 'Papel'])
# Set o nome do papel como indice no dataframe
df.set_index(inplace=True, keys='Papel')

# Trata dataframe para remover caracteres que atrapalham os numeros
df.replace(inplace=True, regex=True, to_replace=r'\%', value='')

# Itera pelo dataframe para deixar os separadores de decimal com .
for column in df.columns:
    if df[column].dtype == 'object':
        df[column].replace(inplace=True, regex=True, to_replace=r'\.',value='')
        df[column].replace(inplace=True, regex=True, to_replace=r'\,',value='.')
        df[column] = pd.to_numeric(df[column])

df['Cotação'] = df['Cotação'] /100

df['Preco Justo Bazin'] = ((df['Div.Yield'] * df['Cotação']) /100) * 16.67
print(df['Preco Justo Bazin'])
# Aplica o Kmeans
kmeans = KMeans(init='k-means++', n_clusters=N_CLUSTERS, n_init=10)
kmeans.fit(df)
pred_classes = kmeans.predict(df)

df['Grupo'] = pred_classes
df.sort_values(['Grupo'], inplace=True)
print(df)

df.to_csv("./data/" + fileName)
#psql = db()
#print(psql)
