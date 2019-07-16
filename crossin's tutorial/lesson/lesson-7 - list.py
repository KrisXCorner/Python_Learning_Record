l = [365,'everyday',0.618,True]

print(l[2])
print(l[0])     #索引从 0 开始，l[0]表示第一项

print(l[-1])    #-1表示倒数第一

print(l[1:3])   #list 的切片，1:3 表示第二到第四项
print(l[1:-1])


sentence = 'Hi Kris, how are you today?'

a = sentence.split()    #split是把一个字符串分割成很多字符串组成的list
b = sentence.split(',')     #默认按空格分割句子，也可以加参数
print(a,b)

s = '; '
li = ['apple', 'pear', 'orange']
fruit = s.join(li)  #join则是把一个list中的所有字符串连接成一个字符串
print(fruit)

';'.join(['apple','pear','orange'])

word = 'hello world'    #字符串的切分与数组类似，但是字符串不能直接赋值
for c in word:
    print(c)