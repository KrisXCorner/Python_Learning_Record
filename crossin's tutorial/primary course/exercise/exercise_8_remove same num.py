# 从一组数据中去除掉重复的元素，并将其排序输出。 

l = [4, 7, 3, 4, 1, 9, 8, 3, 7]

l_2 = sorted(set(l))
print(l_2)


# set 返回一个去重的list
# sorted 返回一个新list，按顺序排练