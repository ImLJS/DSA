# Binary Search Algorithm
# Best case    : 0(1)
# Average case : 0(log n)
# Worst case   : 0(log n)


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
