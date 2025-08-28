# Contain Duplicate II - LeetCode 219 - Medium

# https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Approach 1: Sliding Window with HashSet
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))

def containsNearbyDuplicate(nums, k):
    num_set = set()
    
    for i in range(len(nums)):
        if nums[i] in num_set:
            return True
        num_set.add(nums[i])
        if len(num_set) > k:
            num_set.remove(nums[i - k])
    return False

# Example usage:
print(containsNearbyDuplicate([1,2,3,1], 3))  # Output: True
print(containsNearbyDuplicate([1,0,1,1], 1))  # Output: True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))  # Output: False

# Approach 2: HashMap to store the last seen index
# Time Complexity: O(n)
# Space Complexity: O(n)

def containsNearbyDuplicateHashMap(nums, k):
    index_map = {}
    
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    return False

# Example usage:
print(containsNearbyDuplicateHashMap([1,2,3,1], 3)) # Output: True
print(containsNearbyDuplicateHashMap([1,0,1,1], 1)) # Output: True
print(containsNearbyDuplicateHashMap([1,2,3,1,2,3], 2)) # Output: False