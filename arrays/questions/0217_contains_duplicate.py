# Contains Duplicate - LeetCode 217 - Easy

# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Approach:
# 1. Create an empty set to keep track of seen numbers.
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))  # Output: True
# Example 2:
nums = [1, 2, 3, 4]
print(contains_duplicate(nums))  # Output: False

# Alternative approach using sorting:
def contains_duplicate_sorting(nums: list[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# Example usage:
nums = [1, 2, 3, 1]
print(contains_duplicate_sorting(nums))  # Output: True
# Example 2:
nums = [1, 2, 3, 4]
print(contains_duplicate_sorting(nums))  # Output: False

# Alternative approach using set comparison:
def contains_duplicate_set_comparison(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# Example usage:
nums = [1, 2, 3, 1]
print(contains_duplicate_set_comparison(nums))  # Output: True
# Example 2:
nums = [1, 2, 3, 4]
print(contains_duplicate_set_comparison(nums))  # Output: False