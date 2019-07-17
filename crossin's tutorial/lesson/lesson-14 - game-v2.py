f = open('./lesson/game.txt',encoding='utf-8')
lines = f.readlines()
f.close()

name = input('Enter your name \n')
print('Hello,%s'%name)
scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:    #如果没有找到该玩家的数据，说明他是一个新玩家，我们给他初始化一组成绩
    score = [0,0,0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

def isEqual(num1,num2):
    if num1<num2:
        print(num1)
        print('too small')
        return False
    elif num1>num2:
        print(num1)
        print('too big')
        return False
    else:
        print(num1)
        print('Bingo! You totally guessed',count,'times.')
        return True

from random import randint
a = randint(0,10)
print('Guess an number between 0-10')
bingo = False
count = 0
while bingo == False:
    num = int(input())
    count += 1
    bingo = isEqual(num,a)
    
    if num < 0:
        print('Exit game...')
        break
total_times += count

if game_times == 0 or count < min_times:
    min_times = count

if game_times > 0:
    avg_times = total_times / game_times
else:
    avg_times = 0
game_times += 1

scores[name] = [str(game_times),str(min_times),str(total_times)]      #这里一定要加空格，不如一次输出后分数就连在一块了
result = ''
for n in scores:
    line = n + '' + ''.join(scores[n]) + '\n'
    result += line

print('%s,你一共玩了%d轮，最快%d次猜中，平均%.2f次猜中'%(name,game_times,min_times,avg_times))

f = open('./lesson/game.txt','w',encoding='utf-8')
f.write(result)
f.close()