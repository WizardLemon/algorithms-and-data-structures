import random

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
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

def inorder_tree_walk(x):

    if x != None:
        inorder_tree_walk(x.left)
        print(x.data)
        inorder_tree_walk(x.right)

def tree_search(x, k):

    if x == None or k == x.data:
        return x

    if k < x.data:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def iterative_tree_search(x, k):

    while x != None and k != x.data:
        if k < x.data:
            x = x.left
        else:
            x = x.right

    return x

def tree_minimun(x):

    while x.left != None:
        x = x.left

    return x

def tree_maximum(x):

    while x.right != None:
        x = x.right

    return x

def tree_successor(x):

    if x.right != None:
        return tree_minimun(x.right)
    
    y = x.parent

    while y != None and x == y.right:
        x = y
        y = y.parent
    
    return y

def tree_insert(T, z):

    y = None
    x = T
    
    while x != None:
        y = x

        if z.data < x.data:
            x = x.left
        else: 
            x = x.right

    z.parent = y

    if y == None:
        # tree T was empty
        T.parent = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z

def transplant(T, u, v):

    if u.parent == None:
        T.parent = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v != None:
        v.parent = u.parent

def tree_delete(T, z):

    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimun(z.right)
        
        if y.parent != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y

        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def inorder_tree_walk_insert(x, L):

    if x != None:
        inorder_tree_walk_insert(x.left, L)
        L.append(x.data)
        inorder_tree_walk_insert(x.right, L)