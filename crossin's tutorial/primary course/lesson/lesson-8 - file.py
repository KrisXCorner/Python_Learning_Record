f = open("./lesson/file.txt")    
        #打开一个文件; 与 workspace 所在目录的相对路径
        #python默认是以只读模式打开文件

data = f.read()     #通过read()函数把文件内所有内容读进一个字符串中
print(data)

l2 = f.readlines()
print(l2)

f.close()   #close() 一定要有后面的括号，不然就没有调用这个函数

message = 'Bitcoin to the moon!'
h = open("./lesson/file.txt",'w')    #打开模式为写入;还有一种常用模式是'a'，appending,写入的内容不会覆盖之前的内容，而是添加到原有文件内容后面

h.write(message)
print(h)

h.close()
