import os
from utils import soups_of_interest

def htmlTotxt():
    data_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\html"
    texto_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\texto"
    for file in os.listdir(data_path):
        if(file.endswith(".html")):
            file_path = os.path.join(data_path, file)
            arquivo = open(file_path, "r+", encoding="utf8")
            pag = arquivo.read()
            arquivo.close()
            file_path = os.path.join(texto_path, file[:-4]+"txt")
            arquivo = open(file_path, "w+", encoding="utf8")
            arquivo.write(soups_of_interest(pag))
            arquivo.close
    return

def preprocessing():

    return

htmlTotxt()