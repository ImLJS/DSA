# Longest Decreasing Subsequence

# Given a sequence of numbers, find the longest subsequence that is decreasing.

# This subsequence can "jump" over numbers in the sequence.
# For example in 5, 2, 8, 6, 3, 6, 9, the longest subsequence is 5, 3.

# This is a classic dynamic programming problem. We can solve this problem using dynamic programming.

# Let's define the following notation:

# L(i) = the length of the longest subsequence ending at index i
# L(i) = 1 + max(L(j)) where 0 <= j < i and arr[j] > arr[i]
# The solution is the maximum value of L(i) for all i.

# Let's implement this solution:


def longest_decreasing_subsequence(arr):
    if not arr:
        return []

    n = len(arr)
    # dp[i] stores the length of LDS ending at index i
    dp = [1] * n
    # prev[i] stores the previous index in the LDS ending at i
    prev = [-1] * n

    # Track the index where the longest subsequence ends
    max_length = 1
    max_index = 0

    # Fill dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j] and dp[j] + 1 > dp[i]:
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


# Helper function to demonstrate usage
def demonstrate_lds():
    test_cases = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],
        [10, 9, 8, 7, 6, 5],
        [3, 10, 2, 1, 20],
        [1],
        [],
    ]

    for arr in test_cases:
        result = longest_decreasing_subsequence(arr)
        print(f"Array: {arr}")
        print(f"Longest decreasing subsequence: {result}")
        print(f"Length: {len(result)}\n")


# Example usage
if __name__ == "__main__":
    demonstrate_lds()
