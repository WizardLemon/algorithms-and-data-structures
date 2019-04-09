from functions import *

def main():

    node_val_4 = Node(None, None, None, 4)
    node_val_9 = Node(None, None, None, 9)
    node_val_5 = Node(None, None, None, 5)
    node_val_2 = Node(None, None, None, 2)
    node_val_1 = Node(None, None, None, 1)
    node_val_17 = Node(None, None, None, 17)
    node_val_13 = Node(None, None, None, 13)
    T = Node(None, None, None, 7)

    tree_insert(T, node_val_4)
    tree_insert(T, node_val_9)
    tree_insert(T, node_val_2)
    tree_insert(T, node_val_1)
    tree_insert(T, node_val_17)
    tree_insert(T, node_val_5)
    tree_insert(T, node_val_13)

    inorder_tree_walk(T)
    
    print("\nSuccessor of " + str(node_val_9.data))
    print(tree_successor(node_val_9).data)

    print("\nTesting delete")

    tree_delete(T, node_val_13)

    inorder_tree_walk(T)

    print("\nRandom generated tree")

    myList = random_list(1, 100, 10)

    myT = Node(None, None, None, myList[0])

    nodeList = []
   
    for i in range(1, len(myList)):
        n = Node(None, None, None, myList[i])
        nodeList.append(n)

    for i in range(0, len(nodeList)):
        print(nodeList[i].data)

    for i in range(0, len(nodeList)):
        tree_insert(myT, nodeList[i])

    sortedList = []

    print("Test")

    inorder_tree_walk(myT)

    inorder_tree_walk_insert(myT, sortedList)

    print(myList)
    print(sortedList)

main()