from functions import *

def main():
    myList = random_list(0, 100, 10)

    for i in range(0, len(myList)):
        myList[i] = myList[i] / 100

    print(myList)

    sortedList = bucket_sort(myList)

    print(sortedList)

main()