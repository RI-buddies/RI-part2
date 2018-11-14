#MundoMax - OK

import os 
from collections import defaultdict
from utils import readList

tokens_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\tokens"
index = defaultdict(list)
marcas = ["giannini", "andaluz", "takamine", "crafter", "dean", 
           "epiphone", "fender", "ibanez", "eagle", "phx", "tagima", 
           "class", "sigma", "martin", "madrid", "strinberg", "di giorgio",
           "yamaha", "michael", "vogga", "auburn", "harmonics"]
cordas = ["nylon", "aço", "aco"]
categorias = ["acústico", "acustico", "elétrico", "eletrico","eletroacústico", "eletroacustico"]
escalas = ["rosewood"]
tampos =["basswood", "spruce", "linden"]

def createIndex():
    for file in os.listdir(tokens_path):
        countMarca = countCorda = countCategoria = countEscala = countTampo = 0
        if(int(file[:-4]) > 20 and int(file[:-4]) < 31):
            file_path = os.path.join(tokens_path, file)
            tokens = readList(file_path)
            for token in tokens:
                if token in marcas:
                    countMarca += 1
                    marca = token                        
                elif token in cordas:
                    countCorda += 1
                    if token == "aco":
                        corda = "aço"
                    else:
                        corda = token                    
                elif token in categorias:
                    countCategoria += 1
                    if (token == "eletroacústico") or (token == "eletroacustico") or (token == "eletrico"):
                        categoria = "elétrico"
                    elif token == "acustico":
                        categoria = "acústico"
                    else:
                        categoria = token                    
                elif token in escalas:
                    countEscala += 1
                    escala = token                    
                elif token in tampos:
                    countTampo += 1
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

def writeIndexToFile(): #ver forma de escrever o índice em um árquivo csv
    teste = 1

createIndex()

def showIndexAtts(atributo, atributo_array): #função que imprime os pares atributo-valor do índice invertido de acordo com o atributo escolhido
    if atributo == "Marca":
        for att in atributo_array:
            print("Marca.%s -> " % att, index["Marca."+att])
            input("wait")
    elif atributo == "Corda":
        for att in atributo_array:
            if att != "aco":
                print("Corda.%s -> " % att, index["Corda."+att])
                input("wait")
    elif atributo == "Categoria":
        for att in atributo_array:
            if (att != "acustico") and (att != "eletrico") and (att != "eletroacústico") and (att != "eletroacustico"):
                print("Categoria.%s -> " % att, index["Categoria."+att])
                input("wait")
    elif atributo == "Escala":
        for att in atributo_array:
            print("Escala.%s -> " % att, index["Escala."+att])
            input("wait")
    elif atributo == "Tampo":
        for att in atributo_array:
            print("Tampo.%s -> " % att, index["Tampo."+att])
            input("wait")       

showIndexAtts("Marca", marcas)
showIndexAtts("Corda", cordas)
showIndexAtts("Categoria", categorias)
showIndexAtts("Escala", escalas)
showIndexAtts("Tampo", tampos)

# print("Marca.eagle ->", index["Marca.eagle"])
# input("wait")
# print("Marca.phx -> ", index["Marca.phx"])
# input("wait")
# print("Marca.strinberg -> ", index["Marca.strinberg"])
# input("wait")
# print("Marca.giannini -> ", index["Marca.giannini"])
# input("wait")
# print("Marca.tagima -> ", index["Marca.tagima"])
# input("wait")
# print("Marca.class -> ", index["Marca.class"])
# input("wait")
# print("Corda.nylon -> ", index["Corda.nylon"])
# input("wait")
# print("Corda.aço -> ", index["Corda.aço"])
# input("wait")
# print("Categoria.elétrico -> ", index["Categoria.elétrico"])
# input("wait")
# print("Categoria.acústico -> ", index["Categoria.acústico"])
# input("wait")
# print("Escala.rosewood -> ", index["Escala.rosewood"])
# input("wait")
# print("Tampo.spruce -> ", index["Tampo.spruce"])
# input("wait")
# print("Tampo.basswood -> ", index["Tampo.basswood"])
# input("wait")
# print("Tampo.linden -> ", index["Tampo.linden"])
# input("wait")