postion = (1, 2)
geeks = ('Sheldon', 'Leonard', 'Rajesh', 'Howard')

def get_pos(n):
    return (n/2, n*2)

# 得到这个函数的返回值的两种形式，一种是根据返回值元组中元素的个数提供变量，一种是用一个变量记录返回的元组

x,y = get_pos(50)
print(x)
print(y)

pos = get_pos(50)
print(pos[0])
print(pos[1])