# Concatanation of Array - LeetCode 1929 - Easy

# https://leetcode.com/problems/concatenation-of-array/

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.

# Example 1:
# Input: nums = [1,2,1] 
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
# - ans = [1, 2, 1, 1, 2, 1]

# Approach

def getConcatenation(nums):
    return nums + nums

def getConcatenationAlternative(nums):
    n = len(nums)
    result = [0] * (2 * n)  # Initialize a list of size 2n with zeros
    for i in range(n):
        result[i] = nums[i]        # First half
        result[i + n] = nums[i]    # Second half
    return result

def getConcatenationUsingExtend(nums):
    nums.extend(nums)  # Concatenate nums with itself
    return nums

# Explanation
# 1. The first function uses Python's list concatenation feature to create a new list
#    that is the concatenation of nums with itself.
# 2. The second function initializes a new list of size 2n and fills it by iterating through the original list.
# 3. The third function uses the extend method to append the elements of nums to itself.
# 4. All three functions return the new concatenated list.

# Example usage
nums1 = [1, 2, 1]
print(getConcatenation(nums1))  # Output: [1, 2, 1, 1, 2, 1]
nums2 = [1, 3, 2, 1]
print(getConcatenationAlternative(nums2))  # Output: [1, 3, 2, 1, 1, 3, 2, 1]
nums3 = [2, 5, 1, 3, 4, 7]
print(getConcatenationUsingExtend(nums3))  # Output: [2, 5, 1, 3, 4, 7, 2, 5, 1, 3, 4, 7]
