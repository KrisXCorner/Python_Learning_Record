# 找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹。

import os


def findfile(path,rule = ".txt"):
    txtlist = []
    for fpathe,dirs,fs in os.walk(path):        # os.walk 获取所有目录
        for f in fs:
            filename = os.path.join(fpathe,f)
            #print(filename)
            if filename.endswith(rule):         # 判断是否用 .txt 结尾
                txtlist.append(filename)
    return txtlist

if __name__ == "__main__":
    b = findfile(r"/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/")
    #print(b)
    for i in b:
        print(i)
    print('一共有个 %d 个文件'%len(b))      # len 计算 b 的长度
