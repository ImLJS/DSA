# Maximum Sum Circular Subarray - LeetCode 918 - Medium

# https://leetcode.com/problems/maximum-sum-circular-subarray/

# Used to find the maximum sum of a subarray in a circular array using Kadane's Algorithm for both non-circular and circular cases. The function calculates the maximum sum of a subarray that can wrap around the end of the array to the beginning. It does this by finding the maximum sum of a non-circular subarray and comparing it to the total sum of the array minus the minimum sum of a subarray (which represents the circular case). If all elements are negative, it returns the maximum element.

# Example:
# Input: arr = [5,-3,5]
# Output: 10
# Explanation: The subarray [5,5] has the maximum sum 5 + 5 = 10.

# Time Complexity: O(n)
# Space Complexity: O(1)

def maxSubarraySumCircular(arr):
    maxSum, minSum = arr[0], arr[0]
    curMax, curMin = arr[0], arr[0]
    total = arr[0]
    n = len(arr)
    for i in range(1, n):
        curMax = max(arr[i], curMax + arr[i])
        maxSum = max(maxSum, curMax) 
        curMin = min(arr[i], curMin + arr[i])
        minSum = min(minSum, curMin)
        total += arr[i]
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum

# Example usage
if __name__ == "__main__":
    arr = [5, -3, 5]
    print(maxSubarraySumCircular(arr))  # Output: 10
    arr = [3, -1, 2, -1]
    print(maxSubarraySumCircular(arr))  # Output: 4
    arr = [3, -2, 2, -3]
    print(maxSubarraySumCircular(arr))  # Output: 3
    arr = [-2, -3, -1]
    print(maxSubarraySumCircular(arr))  # Output: -1