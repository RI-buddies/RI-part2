import os
from utils import soups_of_interest
from utils import clean_text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import PorterStemmer

data_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\html"
texto_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\texto"
tokenized_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\tokens"

def htmlTotxt():
    for file in os.listdir(data_path):
        if(file.endswith(".html")):
            file_path = os.path.join(data_path, file)
            arquivo = open(file_path, "r+", encoding="utf8")
            pag = arquivo.read()
            arquivo.close()
            file_path = os.path.join(texto_path, file[:-4]+"txt")
            arquivo = open(file_path, "w+", encoding="utf8")
            arquivo.write(soups_of_interest(pag))
            arquivo.close()

def extractMundoMax():
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 20 and int(file[:-4]) < 31):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if(append == 1):
                        lst.append(line)
                    if("VEJA O REGULAMENTO\n" in line):
                        append = 1
                    if("COMPRAR JUNTO\n" in line):
                        append = 0
                    if("Descrição\n" in line):
                        append = 1
                    if("AVALIAR\n" in line):
                        append = 0

            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractMadeInBrazil():
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 30 and int(file[:-4]) < 41):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if(append == 1):
                        lst.append(line)
                    if("//------------------------- Tratamento do player de video/iframe -----------------------------------//\n" in line):
                        append = 1
                    if("Quantidade\n" in line):
                        append = 0
                    if("informações\n" in line):
                        append = 1
                    if("sobre a marca\n" in line):
                        append = 0
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractPlaytech():
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 30 and int(file[:-4]) < 41):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if(append == 1):
                        lst.append(line)
                    if("//------------------------- Tratamento do player de video/iframe -----------------------------------//\n" in line):
                        append = 1
                    if("Quantidade\n" in line):
                        append = 0
                    if("informações\n" in line):
                        append = 1
                    if("sobre a marca\n" in line):
                        append = 0
            file_path = r"C:\Users\Lucas\Desktop\teste.txt"
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)
            input("wait")


def preprocessing():
    stopWords_p = stopwords.words('portuguese')
    stopWords_e = stopwords.words('english')
    stopWords = stopWords_p + stopWords_e

    for file in os.listdir(texto_path):
        if(file.endswith(".txt")):
            file_path = os.path.join(texto_path, file)
            arquivo = open(file_path, "r+", encoding="utf8")
            pag = arquivo.read()
            arquivo.close()
            
            pag = clean_text(pag) #remove special characters
            pag = pag.lower() #lowercase
            pag = word_tokenize(pag) #tokenize
            pag_aux = [x for x in pag if x not in stopWords] #remove stopwords
            pag = pag_aux

            file_path = os.path.join(tokenized_path, file) 
            arquivo = open(file_path, "w", encoding="utf8")
            arquivo.write(str(pag))
            arquivo.close()

extractMadeInBrazil()