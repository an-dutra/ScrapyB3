#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

maxTry = 10


class Table:
    def __init__(self, url, data, tabNum=0):
        # Isso aqui deve ser convertido pra uma classe - Extract
        # sending post request and saving response as response object
        r = requests.post(url=url, data=data)

        print("Recuperando tabela em html")
        # Extracting tale from html
        soup = BeautifulSoup(r.text, "html.parser")
        tableHtml = soup.find_all('table')
        i = 0
        while not tableHtml:
            tableHtml = soup.find_all('table')
            if maxTry == i:
                self.table = None
                return None
            i += 1
            time.sleep(10)

        tableHtml = tableHtml[tabNum]
        # Generating dataframe
        self.table = pd.read_html(str(tableHtml))[tabNum]

    def get(self):
        return self.table

    def to_csv(self, file_name):
        print(self.table)
        self.table.to_csv(file_name, sep='\t', encoding='utf-8')
