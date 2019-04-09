import random
import time

heapsize = 0

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def parent(i):
    return (i - 1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, i):
    l = left(i)
    r = right(i)

    global heapsize

    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    global heapsize
    heapsize = len(A)
    
    for i in range((len(A) - 1)//2, -1, -1):
        max_heapify(A, i)

def heapsort(A):
    build_max_heap(A)
    global heapsize
    
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize = heapsize - 1
        print(A)
        max_heapify(A, 0)