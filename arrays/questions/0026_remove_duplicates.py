# Remove Duplicates from Sorted Array - LeetCode 26 - Easy

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

# Approach: Compare each element with the previous one and use a pointer to track the position of the next unique element.

# Time Complexity: O(n)
# Space Complexity: O(1)

def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # Pointer for the next position to place a unique element
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # If the current element is different from the previous one
            nums[k] = nums[i]  # Place it at index k
            k += 1
    return k

# Explanation
# 1. Check if the array is empty. If it is, return 0.
# 2. Initialize a pointer k to track the position of the next unique element.
# 3. Iterate through the array starting from the second element:
#    - If the current element is different from the previous one, place it at index k and increment k.
# 4. After the loop, k will represent the new length of the array with unique elements.
# 5. The elements from index 0 to k-1 will be the unique elements, and the rest of the array can be ignored.

# Example usage
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(f"Output: {k1}, nums = {nums1[:k1]} + {['_'] * (len(nums1) - k1)}")
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(f"Output: {k2}, nums = {nums2[:k2]} + {['_'] * (len(nums2) - k2)}")