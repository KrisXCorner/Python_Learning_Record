def fuc(arg1=1,arg2=2,arg3=3):      # 增加了参数的默认值
    print(arg1,arg2,arg3)

fuc()
fuc(3)
fuc(6,arg3=8)
fuc(5,2,6)


#  func(*args) 方式是把参数作为 tuple 传入函数内部(⬇️)

def calcSum(*arg):      # *arg 可以接受任意数量的参数
    sum = 0
    for i in arg:
        sum += i
    print(sum)

calcSum(23,5,7)
calcSum(2)
calcSum()

# 在变量前加上星号前缀（*），调用时的参数会存储在一个 tuple（元组）对象中，赋值给形参
# 有一点需要注意，tuple 是有序的


# func(**kargs) 则是把参数以键值对字典的形式传入
def printAll(**karg):       # 采用这种参数传递的方法，可以不受参数数量、位置的限制
    for k in karg:
        print(k,";",karg[k])

printAll(a=1,b=2,c=6)
printAll(x=4,y=8)

# ——-------------------------------------------------

# 可以混合使用

def func(x, y=5, *a, **b):
    print (x, y, a, b)
    
func(1)
func(1,2)
func(1,2,3)
func(1,2,3,4)
func(x=1)
func(x=1,y=1)
func(x=1,y=1,a=1)
func(x=1,y=1,a=1,b=1)
func(1,y=1)
func(1,2,3,4,a=1)
func(1,2,3,4,k=1,t=2,o=3)


# 在混合使用时，首先要注意函数的写法，必须遵守：

# 1、带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
# 2、元组参数(*args)须在带有默认值的形参(arg=)之后；
# 3、字典参数(**kargs)须在元组参数(*args)之后。


# 调用时也需要遵守：

# 1、指定参数名称的参数要在无指定参数名称的参数之后；
# 2、不可以重复传递，即按顺序提供某参数之后，又指定名称传递。


# 而在函数被调用时，参数的传递过程为：

# 1、按顺序把无指定参数的实参赋值给形参；
# 2、把指定参数名称(arg=v)的实参赋值给对应的形参；
# 3、将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
# 4、将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。