from random import randint

score = 0

direction = ['left','right','middle']
print('choose a direction to shoot:left ? right ? middle ?')
a = input()
b = randint('left','right','middle')

if a == b:
    score -= 1
    print('Pity! Failed to score.')
else:
    score += 1
    print('Congratulations! Nice shoot!')

print('choose a direction to keep:left ? right ? middle ?')

if a == b:
    score += 1
    print('Congratulations! Nice shoot!')
else:
    score -= 1
    print('Pity! Failed to score.')