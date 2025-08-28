# Valid Anagram - LeetCode 242 - Easy

# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Approach:
# 1. If the lengths of the strings are different, return false.
# 2. Create a frequency dictionary for characters in the first string.
# 3. Decrease the frequency for each character found in the second string.
# 4. If any frequency is not zero, return false. Otherwise, return true.

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True

# Example usage:
s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Output: True
# Example 2:
s = "rat"
t = "car"
print(is_anagram(s, t))  # Output: False

