# Binary Search Algorithm
# Best case        : 0(1)
# Average case     : 0(log n)
# Worst case       : 0(log n)
# Space complexity : 0(1)

# Binary search is a searching algorithm that searches a target value within a sorted array. It compares the target
# value to the middle element of the array. If they are not equal, the half in which the target cannot lie is
# eliminated and the search continues on the remaining half, again taking the middle element to compare to the target
# value, and repeating this until the target value is found. If the search ends with the remaining half being empty,
# the target is not in the array.


def binary_search(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return f"Key {key} found at index {mid+1}"
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return f"Key {key} not found"


def binary_search_recursive(arr, key, start, end):
    if start > end:
        return f"Key {key} not found"
    mid = (start + end) // 2
    if arr[mid] == key:
        return f"Key {key} found at index {mid+1}"

    if arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, end)
    else:
        return binary_search_recursive(arr, key, start, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# key = 11
key = 7

print(binary_search(arr, key))
start = 0
end = len(arr) - 1
print(binary_search_recursive(arr, key, start, end))
