from module1 import *

def main():
    input1 = ['a', 'b']
    # print(input1)

    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    # print(input2)

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    # print(input3)

    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    # print(input4)

    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    print(input5)

    histogram = GetHistogram(input5)

    my_list = list(histogram)

    node_list = []

    while(histogram):
        min = GetMinFreqElemHist(histogram)
        node_list.append(Data(min, histogram[min]))
        histogram.pop(min)

    # print(my_list)
    # print(node_list)

    while len(node_list) > 1:
        e1 = GetMinFreqElem(node_list)
        RemoveElem(node_list, e1)
        e2 = GetMinFreqElem(node_list)
        RemoveElem(node_list, e2)
        
        ne = MakeNewElem(e1, e2)
        PutElem(node_list, ne)

    inorder_tree_walk(node_list[0])

    
        
    
        

main()