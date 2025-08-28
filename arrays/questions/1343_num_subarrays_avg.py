# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold - LeetCode 1343 - Medium

# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

# Given an integer array arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

# Example 1:
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: The sub-arrays of size 3 are [2,2,2], [2,2,5], [2,5,5], [5,5,5], [5,5,8] and their averages are 2, 3, 4, 5, 6 respectively. The averages greater than or equal to 4 are [2,5,5], [5,5,5], and [5,5,8].

# Approach: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

def numOfSubarrays(arr, k, threshold):
    target = k * threshold
    count = 0
    window_sum = sum(arr[:k])
    if window_sum >= target:
        count += 1
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum >= target:
            count += 1
            
    return count

# Example usage:
print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))  # Output: 3
print(numOfSubarrays([1,1,1,1,1], 1, 0))  # Output: 5
print(numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))  # Output: 6
print(numOfSubarrays([7,7,7,7,7,7,7], 7, 7))  # Output: 1