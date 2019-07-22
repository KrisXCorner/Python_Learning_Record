def sum(a, b, c):
    return a + b + c
    
print (sum(1, 2, 3))
print (sum(4, 5, 6))

# 等同于

Sum = lambda a,b,c: a+b+c
print (Sum(1, 2, 3))
print (Sum(4, 5, 6))


# 定义 lambda 表达式时，参数列表周围没有括号，返回值前没有 return 关键字，也没有函数名称。
# 它的主体只能是一个表达式，不可以是代码块，甚至不能是命令（print 不能用在 lambda 表达式中）

def fn(x):
    return lambda y:x+y

a = fn(2)
print(a)
print(a(3))
