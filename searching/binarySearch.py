# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if l <= r:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr, mid+1, r, x)
        else:
            return binarySearch(arr, l, mid-1, x)
    else:
        return -1


# Driver Code
arr = [2, 3, 4, 5, 10]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
