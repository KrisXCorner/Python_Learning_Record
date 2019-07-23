# 用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出。

print(";".join([str(i) for i in range(1,101) if i%2==0 and i%3==0 and i%5==0]))