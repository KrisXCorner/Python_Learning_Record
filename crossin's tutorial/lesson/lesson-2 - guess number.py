from random import randint
num = randint(1,10)
print("guess my number")
some = False
count = 0

while some == False:
    count += 1
    answer = int(input())
    if answer > num:
        print('%d is too big!'% answer)
    if answer < num:
        print('%d is too small'% answer)
    if answer == num:
        print('bingo! %d is the right answer.'% answer)
        some = True
print('你一共猜了',count,'次')