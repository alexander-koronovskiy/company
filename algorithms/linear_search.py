# may be realised in for-break-else construction
def linear_search(myList, item):
    for i in range(len(myList)):
        if myList[i] == item:
            return i
    return -1
