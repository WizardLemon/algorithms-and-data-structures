from functions import *

def main():
    myList = random_list(1, 100, 10)
    print(myList)

    heapsort(myList)

    print(myList)
main()