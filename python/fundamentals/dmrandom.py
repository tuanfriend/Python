import random

def randInt(min=0, max=100):
    if min == 0 and max > 0:
        num = random.random()*max
        return num
    elif min > 0 and max == 0:
        num = random.random()*(100-min)+min
        return num
    elif min >= 0 and max >= 0:
        num = random.random()*(max-min)+min
        return num
    else:
        num = random.random()*100
        return num


print(round(randInt(min=0, max=100)))
