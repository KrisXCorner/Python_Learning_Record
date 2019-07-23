from random import choice   #randint 只能随机选整数，choice 是选择一项

score = [0,0]
direction = ['left','center','right']

def kcik():
    print('=== You kick! ===')
    print('choose one side to shoot:left ? center ? right ?')
    you = input()
    ai = choice(direction)

    if you == ai:
        score[1] += 1
        print('Pity! Failed to score.')
    else:
        score[0] += 1
        print('Congratulations! Nice shoot!')
    print('Score:%d(you) vs %d(ai)'%(score[0],score[1]))

    print()
    print('=== You save! ===')
    print("Now it's your turn to save.")
    print('choose one side to save:left ? center? right ?')

    you = input()
    ai = choice(direction)

    if you == ai:
        score[0] += 1
        print('Congratulations! Nice move!')
    else:
        score[1] += 1
        print('Pity! Failed to save.')
    print('Score:%d(you) vs %d(ai)'%(score[0],score[1]))
    print()

for i in range(5):
    print('=== Round %d ===' %(i+1))
    kcik()

while score[0] == score[1]:
    print('Equal! Once more game')
    i += 1
    kcik()

if score[0] > score[1]:
    print('You win!!!')
else:
    print('You lose!')
