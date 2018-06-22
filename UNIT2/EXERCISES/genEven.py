import random
def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''

    while 1:
        even = random.randint(0, 98)
        if even % 2 == 0:
            return even
        
