from random import randint
num = randint(1,10)
print("guess my number")
some = False
count = 0

while some == False:
    count += 1
    answer = int(input())
    if answer > num:
        print('%d is too big!'% answer) #用 %d 字符化整数，%f 字符化为小数，%.2f 保留两位小数
    if answer < num:
        print('%d is too small'% answer)
    if answer == num:
        print(f'bingo! {answer} is the right answer.') #用 f-string 把变量加入到输出里
        some = True
print('你一共猜了',count,'次')