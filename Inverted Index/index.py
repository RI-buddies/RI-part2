import os

text = "testando criação de arquivo"

path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index"
file = open(path+"\\texto.txt", "w+", encoding="utf8")
file.write(text)
file.close()