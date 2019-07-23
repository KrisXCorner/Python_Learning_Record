# 从1~n中，随机取m个数。1<=m<=n 

import random

n = 10
m = 5
a = random.sample(range(1,n),m)
print(a)