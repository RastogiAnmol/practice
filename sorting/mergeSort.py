def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right, mid, n - mid)


def merge(arr, l, r, left_count, right_count):
    i = j = k = 0
    while i < left_count and j < right_count:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i = i + 1
        else:
            arr[k] = r[j]
            j = j + 1
        k = k + 1
    while i < left_count:
        arr[k] = l[i]
        i = i + 1
        k = k + 1

    while j < right_count:
        arr[k] = r[j]
        j = j + 1
        k = k + 1


A = [2, 5, 6, 4, 1, 3, 9, 8, 7, 10]
merge_sort(A)
print(A)
