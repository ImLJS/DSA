# Kadanes Algorithm Template

# Time Complexity: O(n)
# Space Complexity: O(1)

# Kadanes Algorithm is used to find the maximum sum of a subarray in an array.
# It is a dynamic programming algorithm that uses a sliding window approach to solve the problem in
# O(n) time complexity.


# Used to find the maximum sum of a subarray in an array
def kadanes(arr):
    maxSum = arr[0]  # Initialize the maximum sum to the first element of the array
    curSum = arr[0]  # Initialize the current sum to the first element of the array
    n = len(arr)
    for i in range(1, n):
        curSum += arr[i]  # Add the current element to the current sum
        if curSum < 0:  # If the current sum is less than 0, reset the current sum to 0
            curSum = 0
        maxSum = max(maxSum, curSum)  # Update the maximum sum
    return maxSum


# Used to find the indices of the maximum sum subarray in an array
def kadanesSlidingWindow(arr):
    maxSum = arr[0]  # Initialize the maximum sum to the first element of the array
    curSum = 0  # Initialize the current sum to 0
    n = len(arr)
    L = 0  # Initialize the left pointer to 0
    maxL, maxR = 0, 0  # Initialize the maximum left and right pointers to 0
    for R in range(n):
        if curSum < 0:
            curSum = 0
            L = R  # Reset the left pointer to the current right pointer
        curSum += arr[R]  # Add the current element to the current sum
        if (
            curSum > maxSum
        ):  # If the current sum is greater than the maximum sum, update the maximum sum and the maximum left and right pointers
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]  # Return the maximum left and right pointers


arr = [4, -1, 2, -7, 3, 4]

print(kadanes(arr))
print(kadanesSlidingWindow(arr))
