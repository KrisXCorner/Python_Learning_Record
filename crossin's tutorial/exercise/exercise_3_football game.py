from random import choice   #randint 只能随机选整数，choice 是选择一项

score = 0

direction = ['left','center','right']
print('choose one side to shoot:left ? center ? right ?')
you = input()
ai = choice(direction)

if you == ai:
    score -= 1
    print('Pity! Failed to score.')
else:
    score += 1
    print('Congratulations! Nice shoot!')

print()
print("Now it's your turn to keep.")
print('choose one side to keep:left ? center? right ?')

you = input()
ai = choice(direction)

if you == ai:
    score += 1
    print('Congratulations! Nice move!')
else:
    score -= 1
    print('Pity! Failed to keep.')