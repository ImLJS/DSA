# Remove Element - LeetCode 27 - Easy

# https://leetcode.com/problems/remove-element/

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores).

# Approach

# Time Complexity: O(n)
# Space Complexity: O(1)

def removeElement(nums, val):
    k = 0  # Pointer for the next position to place a non-val element
    for i in range(len(nums)):
        if nums[i] != val: # If the current element is not val
            nums[k] = nums[i] # Place it at index k
            k += 1
    return k

# Explanation

# 1. Initialize a pointer k to track the position of the next non-val element.
# 2. Iterate through each element in the array:
#    - If the current element is not equal to val, place it at index k and increment k.
# 3. After the loop, k will represent the new length of the array without val elements.
# 4. The elements from index 0 to k-1 will be the non-val elements, and the rest of the array can be ignored.


# Example usage
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = removeElement(nums1, val1)
print(f"Output: {k1}, nums = {nums1[:k1]} + {['_'] * (len(nums1) - k1)}")



