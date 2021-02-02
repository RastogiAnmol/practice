def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 0:
            break


A = [2, 5, 6, 4, 1, 3, 9, 8, 7, 10]
bubble_sort(A)
print(A)
