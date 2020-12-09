def selection_sort(A):
    for i in range(len(A)):
        temp = i
        mv = A[i]
        for j in range(i, len(A)):
            if A[j] < mv:
                mv = A[j]
                temp = A.index(mv)
        tmp = A[i]
        A[i] = A[temp]
        A[temp] = tmp

    return A


a = [2, 3, 1, 5, 4]

print("unsorted list : {}".format(a))
result = selection_sort(a)
print("sorted list : {}".format(result))