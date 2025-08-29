# Group Anagrams - LeetCode 49 - Medium

# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Algo/DS: Hash Table, String, Sorting

# Time Complexity: O(N * K log K) where N is the number of strings and K is the maximum length of a string. Sorting each string takes O(K log K).
# Space Complexity: O(N * K) for storing the output.

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        # Sort the string to create a key
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())

# Example usage:
strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]
print(groupAnagrams(strs1))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs2))  # Output: [[""]]
print(groupAnagrams(strs3))  # Output: [["a"]]