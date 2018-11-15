#MundoMax - OK
#MadeInBrazil - OK
#Playtech - OK
#MultiSom - OK
#Americanas - OK
#Casas Bahia - OK

import os 
import csv

from collections import defaultdict
from utils import readListFromFile
from utils import readIndexFromCsv
from utils import writeIndexToCsv

from utils import marcas, cordas, categorias, escalas, tampos


tokens_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\tokens"
index_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index"

index = defaultdict(list)

def createIndex():
    print("Criando índice invertido...")
    for file in os.listdir(tokens_path):
        countMarca = countCorda = countCategoria = countEscala = countTampo = 0
        if(int(file[:-4]) > 20 and int(file[:-4]) < 81):
            file_path = os.path.join(tokens_path, file)
            tokens = readListFromFile(file_path)
            for idx, token in enumerate(tokens):
                
                if token in marcas:
                    countMarca += 1
                    if (token == "di"):
                        marca = "di giorgio"
                    else:
                        marca = token

                elif token in cordas:
                    countCorda += 1
                    if token == "aco":
                        corda = "aço"
                    else:
                        corda = token                    

                elif token in categorias:
                    countCategoria += 1
                    if (token == "eletroacústico") or (token == "eletroacustico") or (token == "eletroácustico") or (token == "eletrico"):
                        categoria = "elétrico"
                    elif token == "acustico":
                        categoria = "acústico"
                    else:
                        categoria = token                    
                        
                elif token in escalas:
                    countEscala += 1
                    if token == "jacarandá":
                        escala = "rosewood"
                    elif (token == "pau") and (tokens[idx+1] == "ferro"):
                        escala = "pau ferro"
                    else: 
                        escala = token                    

                elif token in tampos:
                    countTampo += 1
                    if (token == "liden") or (token == "lindan"):
                        tampo = "linden"
                    elif (token == "pinho") or (token == "pine") or (file == "80.txt"):
                        tampo = "spruce"
                    else:
                        tampo = token

            if countMarca != 0:
                index["Marca."+marca].append([int(file[:-4]), countMarca])
            if countCorda != 0:
                index["Corda."+corda].append([int(file[:-4]), countCorda])
            if countCategoria != 0:
                index["Categoria."+categoria].append([int(file[:-4]), countCategoria])
            if countEscala != 0:  
                index["Escala."+escala].append([int(file[:-4]), countEscala])
            if countTampo != 0:
                index["Tampo."+tampo].append([int(file[:-4]), countTampo])   

    writeIndexToCsv(index, index_path) #Escrevendo índice invertido em arquivo .csv

def showIndexAtts(atributo, atributo_array): #função que imprime os pares atributo-valor do índice invertido de acordo com o atributo escolhido
    if atributo == "Marca":
        for att in atributo_array:
            if att != "di":
                print("Marca.%s -> " % att, index["Marca."+att])
                input("wait")
    elif atributo == "Corda":
        for att in atributo_array:
            if att != "aco":
                print("Corda.%s -> " % att, index["Corda."+att])
                input("wait")
    elif atributo == "Categoria":
        for att in atributo_array:
            if (att != "acustico") and (att != "eletrico") and (att != "eletroacústico") and (att != "eletroácustico") and (att != "eletroacustico"):
                print("Categoria.%s -> " % att, index["Categoria."+att])
                input("wait")
    elif atributo == "Escala":
        for att in atributo_array:
            if (att != "jacarandá") and (att != "pau"):
                print("Escala.%s -> " % att, index["Escala."+att])
                input("wait")
    elif atributo == "Tampo":
        for att in atributo_array:
            if (att != "pinho") and (att != "pine") and (att != "liden") and (att != "lindan"):
                print("Tampo.%s -> " % att, index["Tampo."+att])
                input("wait")       

createIndex()

# showIndexAtts("Marca", marcas)
# showIndexAtts("Corda", cordas)
# showIndexAtts("Categoria", categorias)
# showIndexAtts("Escala", escalas)
# showIndexAtts("Tampo", tampos)