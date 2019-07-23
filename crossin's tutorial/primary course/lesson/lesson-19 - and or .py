a = "heaven"
b = "hell"
c = True and a or b
print (c)
d = False and a or b
print (d)

# 在一个bool and a or b语句中，当bool条件为真时，结果是a；当bool条件为假时，结果是b
# 技巧在于，确保a的值不会为假
# 最常用的方式是使 a 成为 [a] 、 b 成为 [b]，然后使用返回值列表的第一个元素

a = ""
b = "hell"
c = (True and [a] or [b])[0]
print (c)

# 在两个常量值进行选择时，and-or会让你的代码更简单