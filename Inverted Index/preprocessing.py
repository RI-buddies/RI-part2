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
