from functions import *

def main():
    myList = random_list()
    sortedList = []

    for i in range(0, len(myList)):
        sortedList.append(0)
    
    print(myList)

    counting_sort(myList, sortedList, len(myList))

    print(sortedList)

main()