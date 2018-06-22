import random

#https://docs.python.org/3/library/random.html

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 
# distributions's equivalent
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

# distributions's equivalent

def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)

# distributions isn't equivalent
