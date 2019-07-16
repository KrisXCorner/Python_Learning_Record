f = open("/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/lesson/score.txt",encoding='utf-8')
lines = f.readlines()
#print(lines)
f.close()

results = []     #初始化results，给它一个定义（空字符串）

for line in lines:
    data = line.split()
    #print(data)

    sum = 0
    score_list = data[1:]
    for score in score_list:
        sum += int(score)
    
    result = '%s\t:%d\n' %(data[0],sum)
    print(result)
    results.append(result)

#print(results)

out = open("/Users/hangzhang/Desktop/Coding/Python_Learning_Record_1/crossin's tutorial/lesson/final_score.txt",'w',encoding='utf-8')
out.writelines(results)
out.close()