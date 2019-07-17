import os

a = os.getcwd()
print(a)


f = open("./lesson/file.txt")    

data = f.read()   
print(data)

f.close() 