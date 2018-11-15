import os
from utils import readListFromFile

texto_path = r"C:\Users\Lucas\Documents\EC\10º Período\RI\Projeto2\RI-part2\Inverted Index\data\texto"

for file in os.listdir(texto_path):
        if(int(file[:-4]) > 50 and int(file[:-4]) < 61):
            print(int(file[:-4]))
            file_path = os.path.join(texto_path, file)
            lst = []
            append = 0
            with open(file_path, "r", encoding="utf8") as fin:
                a = enumerate(fin)
                print(a)
                # for idx, line in enumerate(fin):
                #     print("IDX ->", idx, "\nLine ->S", line)
                #     print("IDX + 1 ->", idx+1, "\nLINE + 1 ->", fin[idx+1])
                #     input("wait")            

