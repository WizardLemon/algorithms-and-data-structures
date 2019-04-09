import random
import time
import math

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

def bucket_sort(A):
    B = []
    C = []
    n = len(A)

    for i in range(0, n):
        B.append([])

    for i in range(0, n):
        B[math.floor((n*A[i]))].append(A[i])

    for i in range(0, n):
        insertion_sort(B[i])

    for i in range(0, len(B)):
        for j in range(0, len(B[i])):
            C.append(B[i][j])

    return C