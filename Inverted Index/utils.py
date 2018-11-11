import os
import re
import urllib.request

from bs4 import BeautifulSoup

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

def readList(file_path):
    with open(file_path, "r") as file:
        data = eval(file.readline())
        print(data)
    return data