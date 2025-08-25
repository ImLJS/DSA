# Roman to Integer - LeetCode 0013 - Easy

# https://leetcode.com/problems/roman-to-integer/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.
# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "IV"
# Output: 4

# Approach: Use a dictionary to map Roman numerals to integers and iterate through the string, adding or subtracting values based on the rules.

# Time Complexity: O(n)
# Space Complexity: O(1)

def romanToInt(self, s: str) -> int:
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    total = 0

    for index,value in enumerate(s):
        if index+1<len(s):
            if roman[value]>=roman[s[index+1]]:
                total+=roman[value]
            else:
                total-=roman[value]
        else:
            total+=roman[value]

    return total

# Explanation
# 1. Create a dictionary to map each Roman numeral to its integer value.
# 2. Initialize a variable total to store the final integer value.
# 3. Iterate through each character in the string s:
#    - If the current character's value is greater than or equal to the next character's
#      value, add it to total.
#    - If the current character's value is less than the next character's value, subtract
#      it from total.
#    - If it's the last character, simply add its value to total.
# 4. Return the total as the final integer value.

# Example usage
print(romanToInt(None, "III"))  # Output: 3
print(romanToInt(None, "IV"))   # Output: 4
print(romanToInt(None, "IX"))   # Output: 9
print(romanToInt(None, "LVIII")) # Output: 58
print(romanToInt(None, "MCMXCIV")) # Output: 1994
print(romanToInt(None, "XLII")) # Output: 42
print(romanToInt(None, "CDXLIV")) # Output: 444