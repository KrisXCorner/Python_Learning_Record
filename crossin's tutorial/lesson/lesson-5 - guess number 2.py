def isEqual(num1,num2):
    if num1<num2:
        print('too small')
        return False
    if num1>num2:
        print('too big')
        return False
    if num1==num2:
        print('Bingo! You totally guessed',count+1,'times.')
        return True

from random import randint
a = randint(0,10)
print('guess an number')
bingo = False
count = 0

while bingo == False:
    num = int(input())
    bingo = isEqual(num,a)
    count += 1
    