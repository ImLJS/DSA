# Linear Search Algorithm
# Best case    : 0(1)
# Average case : 0(n)
# Worst case   : 0(n)
# Space complexity : 0(1)


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return f"Key {key} found at index {i+1}"
    return f"Key {key} not found"


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# key = 11
key = 7

print(linear_search(arr, key))
