# map 是 Python 自带的内置函数，它的作用是把一个函数应用在一个（或多个）序列上，把列表中的每一项作为函数输入进行计算，再把计算的结果以列表的形式返回。
# map 的第一个参数是一个函数，之后的参数是序列，可以是 list、tuple。

# 看两个问题：

#1. 假设有一个数列，如何把其中每一个元素都翻倍？
#2. 假设有两个数列，如何求和？

lst_1 = [1,4,3,6,7,8]

# ————————————— method 1
lst_2 = [i*2 for i in lst_1]
print(lst_2)


# ————————————— method 2 _ 采用map写法
def double_fuc(x):
    return x*2
lst_3 = map(double_fuc,lst_1)
print(list(lst_3))


# ————————————— method 3 _ 采用 map+lambda 写法
lst_4 = map(lambda x:x*2,lst_1)
print(list(lst_4))


# ————————————— question 2
lst_5 = map(lambda x,y:x+y,lst_1,lst_2)
print(list(lst_5))
