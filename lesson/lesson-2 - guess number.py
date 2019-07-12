from random import randint
num = randint(1,10)
print("guess my number")
some = False
count = 0

while some == False:
    count += 1
    answer = int(input())
    if answer > num:
        print('too big!')
    if answer < num:
        print('too small')
    if answer == num:
        print('bingo')
        some = True
print('你一共猜了',count,'次')