# Longest Increasing Subsequence

# Given a sequence of numbers, find the longest subsequence that is increasing.
# This subsequence can "jump" over numbers in the sequence. For example in 1, 3, 2, 5, 4,
# the longest subsequence is 1, 2, 4.

# This is a classic dynamic programming problem. We can solve this problem using dynamic programming.

# Let's implement this solution:


def longest_increasing_subsequence(arr):
    if not arr:
        return []

    n = len(arr)
    # dp[i] stores the length of LIS ending at index i
    dp = [1] * n
    # prev[i] stores the previous index in the LIS ending at i
    prev = [-1] * n

    # Track the index where the longest subsequence ends
    max_length = 1
    max_index = 0

    # Fill dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
                if dp[i] > max_length:
                    max_length = dp[i]
                    max_index = i

    # Reconstruct the subsequence
    result = []
    curr_index = max_index
    while curr_index != -1:
        result.append(arr[curr_index])
        curr_index = prev[curr_index]

    return result[::-1]  # Reverse to get correct order


# Optimized O(n log n) solution using binary search
def longest_increasing_subsequence_optimized(arr):
    if not arr:
        return []

    n = len(arr)
    # tails[i] stores the smallest value that can end an increasing subsequence of length i+1
    tails = []
    # prev[i] stores the previous index in the LIS ending at i
    prev = [-1] * n
    # index_map[i] stores the index in the original array for the value at tails[i]
    index_map = []

    def binary_search(target):
        left, right = 0, len(tails) - 1
        while left <= right:
            mid = (left + right) // 2
            if tails[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    for i, num in enumerate(arr):
        pos = binary_search(num)

        if pos == len(tails):
            tails.append(num)
            index_map.append(i)
        else:
            tails[pos] = num
            index_map[pos] = i

        prev[i] = index_map[pos - 1] if pos > 0 else -1

    # Reconstruct the sequence
    result = []
    curr_index = index_map[-1]
    while curr_index != -1:
        result.append(arr[curr_index])
        curr_index = prev[curr_index]

    return result[::-1]


# Helper function to demonstrate usage
def demonstrate_lis():
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7],
        [1],
        [],
    ]

    for arr in test_cases:
        result1 = longest_increasing_subsequence(arr)
        result2 = longest_increasing_subsequence_optimized(arr)
        print(f"Array: {arr}")
        print(f"LIS (O(n²)): {result1}")
        print(f"LIS (O(n log n)): {result2}")
        print(f"Length: {len(result1)}\n")


# Example usage
if __name__ == "__main__":
    demonstrate_lis()
