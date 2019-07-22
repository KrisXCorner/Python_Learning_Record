list_1 = [1,2,6,3,6,8,4,7,9]
list_2 = []
for i in list_1:
    if i%2 == 0:
        list_2.append(i)
print(list_2)


# 使用「列表解析」实现同样的效果：

list_3 = [i for i in list_1 if i%2 == 0]
print(list_3)