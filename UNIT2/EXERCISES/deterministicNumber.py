def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed("Hola mami") 
    return 2 * random.randint(5, 10)
