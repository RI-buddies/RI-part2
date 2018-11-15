import os
from utils import readListFromFile

texto_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\texto"

import re
text = "PythonTutorialAndExercises"
lst = []
file_path = os.path.join(texto_path, "69.txt")
with open(file_path, "r", encoding="utf8") as fin:
    for line in fin:
        lista = re.findall('[A-Z][^A-Z]*', line)
        lst.extend(lista)

file_path = r"C:\Users\Lucas\Desktop\teste.txt"
with open(file_path, "w", encoding="utf8") as fout:
    for i in lst:
        fout.write(i)
        fout.write(" ")
