# 把一段字符串用“右起竖排”的古文格式输出，并且拿竖线符号作为每一列的分割符。

words = "静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡。"


for i in range(5):
    temstr = '|'.join([words[j] for j in range(0,len(words)) if j%6 ==i][::-1])
    print(temstr)


#poem_list = list(words)
#print(poem_list)