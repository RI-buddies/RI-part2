import os
import re
import csv
import urllib.request

from bs4 import BeautifulSoup

marcas = ["giannini", "andaluz", "takamine", "crafter", "dean", 
           "epiphone", "fender", "ibanez", "eagle", "phx", "tagima", 
           "sigma", "martin", "madrid", "strinberg", "di", "di giorgio",
           "yamaha", "michael", "vogga", "auburn", "harmonics"]
cordas = ["nylon", "aço", "aco"]
categorias = ["acústico", "acustico", "elétrico", "eletrico"
             ,"eletroacústico", "eletroacustico", "eletroácustico"]
escalas = ["rosewood", "jacarandá", "pau", "pau ferro", 
           "richlite", "hardwood"]
tampos =["basswood", "spruce", "linden", "liden", "pinho", 
         "pine", "birch", "cedar"]

def soups_of_interest(html):
    soup = BeautifulSoup(html, features='lxml')
    for script in soup(["style", "scritp"]):
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    # print (text)
    return text

def clean_text(text):
    x = ['/', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '|', '=', ':', '\\', '*', '>', '<', '@',
    '&', '-']
    for a in x:
        text = text.replace(a, " ")
    return text

def readListFromFile(file_path):
    with open(file_path, "r", encoding="utf8") as file:
        data = eval(file.readline())
        # print(data)
    return data

def writeIndexToCsv(index, index_path): 
    print("Escrevendo index em arquivo .csv...")
    file_path = os.path.join(index_path, "index.csv")
    with open(file_path, "w", encoding = "utf8", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in index.items():
            writer.writerow([key, value])

def readIndexFromCsv(index_path):
    print("Lendo index do arquivo .csv...")
    file_path = os.path.join(index_path, "index.csv")
    with open(file_path, 'r', encoding="utf8") as csv_file:
        reader = csv.reader(csv_file)
        index = dict(reader)
    return index
