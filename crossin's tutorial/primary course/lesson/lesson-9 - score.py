f = open("/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/lesson/score.txt",encoding='utf-8')
#如果是 Mac 或 Linux 系统，浏览器的中文编码多使用 utf-8），则使用 utf-8 编码
lines = f.readlines()   #用readlines，把每一行分开
#print(lines)
f.close()

results = []     #初始化results，给它一个定义（空字符串）

for line in lines:
    data = line.split()     #按照空格，把姓名、每次的成绩分割开
    #print(data)

    sum = 0
    score_list = data[1:]
    for score in score_list:
        sum += int(score)   #score是一个字符串，为了做计算，需要转成整数值int
    
    result = '%s\t:%d\n' %(data[0],sum)
    print(result)
    results.append(result)

#print(results)

out = open("/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/lesson/final_score.txt",'w',encoding='utf-8')
out.writelines(results)     #因为results是一个字符串组成的list，这里我们直接用writelines方法
out.close()