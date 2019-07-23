f = open("/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/lesson/file.txt")
h = open("/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/lesson/file_2_bitcoin.txt",'a')
g = open("/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/lesson/file_3.txt",'w')

data = f.read()
h.write(data)
g.write(data)

f.close()
h.close()
g.close()