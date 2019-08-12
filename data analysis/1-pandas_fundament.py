import pandas as pd         # 利用pandas模块进行操作

df = pd.read_excel('奖励名单 核对.xlsx')        #默认读取到这个Excel的第一个表单
df_1 = pd.read_excel('奖励名单 核对.xlsx',sheet_name = '兑换码')      #指定读取到这个Excel的某个表单
df_2 = pd.read_excel('奖励名单 核对.xlsx',sheet_name = 1)      #指定读取到这个Excel的第二个表单
df_3 = pd.read_excel('奖励名单 核对.xlsx',sheet_name = [0,1])      #指定读取多个表单

data = df.head()     #默认读取前5行的数据
data_eq = df[:5]    #前5行
#print(data_eq)

data_1 = df.tail()      #读取后5行
data_1_eq = df[-5:]

data_2 = df_2    #获取所有的数据
print("{0}".format(data_2))

#1：读取指定的单行，数据会存在列表里面
data_3 = df_2[:4].values      #0表示第一行 这里读取数据并不包含表头，要注意哦！
#print("读取指定行的数据为\n{0}".format(data_2)) 