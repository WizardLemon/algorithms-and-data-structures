from functions import *

def main():
    myList = randomList(1, 100, 10)
    print(myList)

    start_time = time.clock()
    
    randomizedQuicksort(myList, 0, len(myList) - 1)

    end_time = time.clock() - start_time

    print(myList)
    print("Time to sort: " + str(end_time))    

main()