import os
import re
from utils import soups_of_interest
from utils import clean_text
from utils import readListFromFile
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import PorterStemmer

data_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\html"
texto_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\texto"
tokenized_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\tokens"

def htmlTotxt():
    print("Convertendo páginas HTML em texto...")
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

def extractMilSons():
    print("Extraindo texto de 'MilSons'...")
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 0 and int(file[:-4]) < 11):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if "Home" in line:
                        append = 1
                    if "Saiba mais sobre este produto\n" in line:
                        append = 0
                    if "Descrição\n" in line:
                        append = 1
                    if ("Quem viu, também viu" in line) or ("Cadastre-se" in line):
                        append = 0
                    if(append == 1):
                        lst.append(line)
            
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractNovaMusic():
    print("Extraindo texto de 'MilSons'...")
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 10 and int(file[:-4]) < 21):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if ("Início" in line) or ("Etiquetas" in line):
                        append = 1
                    if ("à vista" in line) or ("Esgotado" in line) or ("Compartilhe isso:" in line):
                        append = 0
                    if "Descrição do" in line:
                        append = 1
                    if ("Produtos relacionados" in line) or ("Cadastre-se" in line):
                        append = 0
                    if(append == 1):
                        lst.append(line)
           
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractMundoMax():
    print("Extraindo texto de 'MundoMax'...")
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
                        lst.append(line)
                        append = 1
                    if("COMPRAR JUNTO\n" in line):
                        append = 0
                    if("Descrição\n" in line) or ("Características\n" in line):
                        lst.append(line)
                        append = 1
                    if("AVALIAR\n" in line) or ("Quantidade no kit: 1 UNIDADE\n" in line):
                        append = 0

            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractMadeInBrazil():
    print("Extraindo texto de 'MadeInBrazil'...")
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 30 and int(file[:-4]) < 41):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if append == 1:
                        lst.append(line)
                    if "Home\n" in line:
                        lst.append(line)
                        append = 1
                    if "// Insere função no array" in line:
                        append = 0
                    if "//------------------------- Tratamento do player de video/iframe -----------------------------------//\n" in line:
                        lst.append(line)
                        append = 1
                    if "Quantidade\n" in line:
                        append = 0
                    if "informações\n" in line:
                        lst.append(line)
                        append = 1
                    if "sobre a marca\n" in line:
                        append = 0

            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractPlaytech():
    print("Extraindo texto de 'Playtech'...")
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 40 and int(file[:-4]) < 51):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if(append == 1):
                        lst.append(line)
                    if("Home\n" in line):
                        lst.append(line)
                        append = 1
                    if("Clique aqui para imagem ampliada\n" in line):
                        append = 0
                    if("Descrição\n" in line):
                        lst.append(line)
                        append = 1
                    if("Pergunte e veja as opiniões de quem já comprou\n" in line):
                        append = 0

            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractMultiSom():
    print("Extraindo texto de 'MultiSom'...")
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 50 and int(file[:-4]) < 61):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = aux = 0            
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if append == 1:
                        lst.append(line)
                    if "facebook-jssdk" in line:
                        lst.append(line)
                        append = 1
                    if "CÓD." in line:
                        append = 0
                    if (aux == 1) and (("Garantia" in line) or ("Especificação Técnica" in line)):
                        lst.append(line)
                        append = 1
                        aux = 0
                    if "Descrição\n" in line:
                        aux = 1
                    if ("Você pode gostar também\n" in line) or ("Avaliar este produto\n" in line):
                        append = 0

            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

def extractAmericanas():
    print("Extraindo texto de 'Americanas'...")
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 60 and int(file[:-4]) < 71):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0            
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if append == 1:
                        lst.append(line)
                    if "Americanas.comBusca BuscarCancelar" in line:
                        lst.append(line)
                        append = 1
                    if "var initPhotoSwipeFromDOM" in line:
                        append = 0
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)
                        
            lst = []
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    lista = re.findall('[A-Z][^A-Z]*', line)
                    lst.extend(lista)
            
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)
                    fout.write(" ")

def extractCasasBahia():
    print("Extraindo texto de 'Casas Bahia'...")
    for file in os.listdir(texto_path):
        if(int(file[:-4]) > 70 and int(file[:-4]) < 81):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0            
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    if append == 1:
                        lst.append(line)
                    if "Cód." in line:
                        lst.append(line)
                        append = 1
                    if "TudoAzul" in line:
                        append = 0
                    if ("Detalhes do produto" in line):
                        lst.append(line)
                        append = 1
                    if("POWERREVIEWS.display.engine" in line):
                        append = 0
            
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)

            lst = []
            with open(file_path, "r", encoding="utf8") as fin:
                for line in fin:
                    lista = re.findall('[A-Z][^A-Z]*', line)
                    lst.extend(lista)
            
            with open(file_path, "w", encoding="utf8") as fout:
                for i in lst:
                    fout.write(i)
                    fout.write(" ")

def tokenize():
    print("Criando arquivo de tokens...")
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

            if(int(file[:-4]) > 70 and int(file[:-4]) < 81):
                file_path = os.path.join(tokenized_path, file)
                tokens = readListFromFile(file_path)
                while 'birch' in tokens:
                    tokens.remove('birch')
                
                with open(file_path, "w", encoding="utf8") as fout:
                    fout.write(str(tokens))

def preProcessing():
    htmlTotxt()
    extractMilSons()
    extractNovaMusic()
    extractMundoMax()
    extractMadeInBrazil()
    extractPlaytech()
    extractMultiSom()
    extractAmericanas()
    extractCasasBahia()        
    tokenize()

if __name__ == "__main__":
    preProcessing()