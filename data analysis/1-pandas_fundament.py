import pandas as pd         # 利用pandas模块进行操作

## 读取数据

df = pd.read_excel('奖励名单 核对.xlsx')        #默认读取到这个Excel的第一个表单
df_1 = pd.read_excel('奖励名单 核对.xlsx',sheet_name = '兑换码')      #指定读取到这个Excel的某个表单
df_2 = pd.read_excel('奖励名单 核对.xlsx',sheet_name = 1)      #指定读取到这个Excel的第二个表单
df_3 = pd.read_excel('奖励名单 核对.xlsx',sheet_name = [0,1])      #指定读取多个表单


## 显示数据

df.shape()       #显示数据的行与列数
df.columns()     #显示列名
df.isnull()      #显示缺失值

data = df.head()     #默认读取前5行的数据
data_eq = df[:5]    #前5行
#print(data_eq)

data_1 = df.tail()      #读取后5行
data_1_eq = df[-5:]

data_2 = df_2['兑奖码'] #读取指定的单列


## 数据清洗

df.dropna(how = 'any')      #删除空值
df.fillna(value = 0)        #用0填充空值
df.rename(columns = {‘核销':'是否核销'})    #重命名列
df['兑换码'].drop_duplicates()      #删除重复值，保留第一次出现的值
df['兑换码'].drop_duplicates(keep = 'last')     #删除重复值，保留最后一次出现的值


## 数据提取

df.loc[0:3]         #提取0-3行的数据
df.iloc[:4,:1]      #4行1列的数据
df.iloc[[3,6,8],[0,1]]      #[3,6,8]代表指定行，[0,1]代表指定列

df['兑换码'].isin(['A3'])       #判断‘兑换码’列里是否包含 A3 的数据
df.loc[df['兑换码'].isin(['A3','M4'])]      #把符合条件的提取出来

df.query('兑换码' == ['A4','M4'])       #query函数查询


## 数据汇总

df.groupby('兑换码').count()
df.groupby('兑换码').sum()      #分组并求和
df.groupby('兑换码').mean()     #分组并求平均
df.sample(n=3)      # 随机取样 3个

df.describe().round(2).T        #自动生成数据的数量，均值，标准差等数据; #round（2）,显示小数点后面2位数，T转置
df['兑换码'].std()          #标准差std()
df['客服当天回复消息数'].cov(df['客服提问数'])      #协方差cov
df['客服当天回复消息数'].corr(df['客服提问数'])     #相关性分析corr ; 相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关

% matplotlib inline
df.plot(kind = 'bar')       #条形图
df.plot()               #默认为折线图