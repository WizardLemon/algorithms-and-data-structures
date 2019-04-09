import random
import time

def random_list():
    list = [random.choice(range(10)) for i in range(10)]
    return list

def counting_sort(A, B, k):
    C = []

    for i in range(0, k):
        C.append(0)

    for j in range(0, len(A)):
        C[A[j]] += 1

    # print(C)

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    # print(C)

    for j in range(0, k):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1