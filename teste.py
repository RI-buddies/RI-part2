def dictionary():
    dicionario = {"rosewood.escala": [[1,2]]}

    print(dicionario["rosewood.escala"])
    dicionario["rosewood.escala"].append([3,9])
    dicionario["rosewood.escala"].append([5,10])
    print(dicionario["rosewood.escala"])
    dicionario["linden.tampo"] = [[2,5]]
    print(dicionario)

file_path = r"C:\Users\Lucas\Desktop\teste.txt"
file = open(file_path, "w", encoding="utf8")
for i in range(1, 10):
    file.write(str(i))
    input("wait")
file.close()