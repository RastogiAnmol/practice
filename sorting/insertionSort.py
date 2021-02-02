def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j+1] = key


A = [2, 5, 6, 4, 1, 3, 9, 8, 7, 10]
insertion_sort(A)
print(A)
