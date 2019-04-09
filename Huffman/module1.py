class Data:
    """
    Data class: Key and frequency of appearing
    """
    def __init__(self, val, f = 0):
        self.value = val
        self.freq = f

    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.freq > other.freq:
            return True
        else:
            return False

    def __str__(self, **kwargs):
        return ("Value: " + str(self.value) + " Frequency: " + str(self.freq))

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.freq = d

    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.freq > other.freq:
            return True
        else:
            return False

    def __str__(self, **kwargs):
        return ("Value: parent" + " Frequency: " + str(self.freq))

    

def GetHistogram(L):

    histogram = {}
    
    for i in range(0, len(L)):
        histogram[L[i]] = 0

    for i in range(0, len(L)):
        histogram[L[i]] += 1

    for k, v in histogram.items():
        print("Value: " + k)
        print("Frequency: " + str(v))

    return histogram

def GetMinFreqElemHist(H):

    L = list(H)

    min = L[0]
    
    for k, v in H.items():
        if H[min] > v:
            min = k

    # print(min)

    return min

def GetMinFreqElem(L):
    return L[0]

def RemoveElem(L, e):
    L.remove(e)
    
def MakeNewElem(e1, e2):
    if e1 < e2:
        return Node(None, e1, e2, e1.freq + e2.freq)
    else:
        return Node(None, e2, e1, e1.freq + e2.freq)

def PutElem(L, ne):
    if len(L) == 0:
        L.append(ne)
    else:
        i = 0
    
        for i in range(0, len(L)):
            if L[i].freq > ne.freq:
                L.insert(i - 1, ne)
                break

        if i == (len(L) - 1):
            L.insert(i, ne)

def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x)
        inorder_tree_walk(x.right)