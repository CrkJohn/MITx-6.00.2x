import operator
def greedy_cow_transport(cows,limit):
    sortedCows = [list(x) for x in sorted(cows.items(), key=operator.itemgetter(1),reverse = True)]
    result   = list()
    while(1):
        sumaCows = sum([cowTons for cow,cowTons in sortedCows])
        if sumaCows == 0:
            break
        limitPrevio = 0
        tmpSortedCows = list()
        tmp  = list()
        for cow,cowTons in sortedCows:
            if cowTons+limitPrevio<=limit:
                limitPrevio+=cowTons
                tmp.append(cow)
            else:
                tmpSortedCows.append([cow,cowTons])
        result.append(tmp)
        sortedCows = tmpSortedCows
    return result
