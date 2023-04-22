import hashlib
import os

def counthash(filepath):
    return hashlib.md5(open(filepath, 'rb').read()).hexdigest()

with open(os.getcwd() + '/signature.txt') as f:
    signatureBase = f.readlines()

folderpath = input("Укажите путь к папке: ")

for filename in os.listdir(folderpath):
    if os.path.isdir(filename) == False:
        try:
            filepath = folderpath + "/" + filename
            hashsum = counthash(filepath)
            if hashsum in signatureBase:

                print("Файл " + filepath + " заражен: " + hashsum)
                
                res = input("Удалить файл? (Y/N) ")
                if res == "Y":
                    os.remove(filepath)
            else:
                print(filepath, hashsum)
        except PermissionError as error:
            print(error)
