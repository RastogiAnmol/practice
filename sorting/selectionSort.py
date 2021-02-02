def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]


A = [2, 5, 6, 4, 1, 3, 9, 8, 7, 10]
selection_sort(A)
print(A)
