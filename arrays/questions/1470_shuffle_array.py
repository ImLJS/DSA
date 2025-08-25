# Shuffle the Array - LeetCode 1470 - Easy

# https://leetcode.com/problems/shuffle-the-array/

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

# Approach: Iterate through the first half and second half of the array simultaneously and append elements to the result.

# Time Complexity: O(n)
# Space Complexity: O(n)

def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])       # Append x_i
        result.append(nums[i + n])   # Append y_i
    return result

# Explanation
# 1. Initialize an empty list result to store the shuffled elements.
# 2. Iterate through the first n elements of the array:
#    - Append the element at index i (x_i) to result.
#    - Append the element at index i + n (y_i) to result.
# 3. After the loop, result will contain the elements in the desired shuffled order.
# 4. Return the result list.

# Example usage
nums1 = [2, 5, 1, 3, 4, 7]
n1 = 3
print(shuffle(nums1, n1))  # Output: [2, 3, 5, 4, 1, 7]
nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
n2 = 4
print(shuffle(nums2, n2))  # Output: [1, 4, 2, 3, 3, 2, 4, 1]
nums3 = [1, 1, 2, 2]
n3 = 2
print(shuffle(nums3, n3))  # Output: [1, 2, 1, 2]