import random

random.randint(1,10)
# 生成一个a到b间的随机整数

random.random()
# 生成一个0到1之间的随机浮点数，包括0但不包括1，也就是[0.0, 1.0)

random.uniform(1.5, 3)  # 生成a、b之间的随机浮点数
random.uniform(3, 1.5)  # 这两种参数都是可行的
random.uniform(1.5, 1.5)    # 永远得到1.5

random.choice([1,3,6,8])      # 从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串

random.randrange(start, stop, step)     # 生成一个从start到stop（不包括stop），间隔为step的一个随机数。start、stop、step都要为整数
random.randrange(4)     # 默认是从0开始，间隔为1

random.sample(population, k)    # 从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列
random.shuffle(x)       # 把序列x中的元素顺序打乱。shuffle直接改变原有的序列。

# 在python中，默认用系统时间作为seed。你也可以手动调用random.seed(x)来指定seed。