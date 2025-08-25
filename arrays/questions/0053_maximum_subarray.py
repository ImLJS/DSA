# Maximum Subarray - LeetCode 53 - Medium

# https://leetcode.com/problems/maximum-subarray/

# Used to find the maximum sum of a subarray in an array

# Kadane's Algorithm

# Example:
# Input: arr = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

# Time Complexity: O(n)
# Space Complexity: O(1)

def kadanes(arr):
    maxSum = arr[0]  # Initialize the maximum sum to the first element of the array
    curSum = 0  # Initialize the current sum to 0

    for i in arr:
        curSum += i  # Add the current element to the current sum
        maxSum = max(maxSum, curSum)  # Update the maximum sum
        if curSum < 0:  # If the current sum is less than 0, reset it to 0
            curSum = 0
    return maxSum


# Example usage

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadanes(arr))  # Output: 6
    
