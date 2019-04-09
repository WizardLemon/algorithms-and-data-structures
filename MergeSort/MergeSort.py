from functions import *

def main():
    test = math.inf
    
    myList = randomList(1, 100, 10)
    print(myList)

    mergeSort(myList, 0, len(myList) - 1)

    print(myList)

main()